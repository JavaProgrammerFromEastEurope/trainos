from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from threading import RLock

from .command_event import CommandEvent
from .event_service import CommandEventService
from .event_type import CommandEventType


@dataclass(frozen=True, slots=True)
class ExecutionDiagnostic:
    """Latest diagnostic event plus recurrence metadata for its retained group."""

    event_id: str
    execution_id: str
    code: str
    severity: str
    message: str
    timestamp_iso: str
    sequence: int | None = None
    occurrences: int = 1
    first_seen_iso: str | None = None

    @property
    def repeated(self) -> bool:
        return self.occurrences > 1


@dataclass(frozen=True, slots=True)
class ExecutionDiagnosticSummary:
    """Summary of the diagnostic groups currently retained for one execution.

    This is intentionally a bounded-retention view, not a durable or lifetime
    per-execution audit. Cumulative lifetime counts remain available globally.
    """

    execution_id: str
    retained_groups: int
    repeated_groups: int
    retained_occurrences: int
    repeated_occurrences: int
    severity_counts: tuple[tuple[str, int], ...]


@dataclass(frozen=True, slots=True)
class ExecutionDiagnosticSnapshot:
    """Immutable view of diagnostic monitoring state."""

    total_events: int
    malformed_events: int
    severity_counts: tuple[tuple[str, int], ...]
    recent_findings: tuple[ExecutionDiagnostic, ...]

    @property
    def critical_count(self) -> int:
        return dict(self.severity_counts).get("critical", 0)

    @property
    def error_count(self) -> int:
        return dict(self.severity_counts).get("error", 0)

    @property
    def repeated_groups_count(self) -> int:
        return sum(finding.repeated for finding in self.recent_findings)

    @property
    def repeated_occurrences_count(self) -> int:
        return sum(max(0, finding.occurrences - 1) for finding in self.recent_findings)


class ExecutionDiagnosticMonitor:
    """Aggregate integrity diagnostic events without mutating execution history.

    Event/severity counts are cumulative for this monitor instance. Retained
    findings are bounded and represent the latest event for each
    (execution_id, code) pair, including a recurrence count for that retained
    group. If a group is evicted, its recurrence metadata is evicted too. The
    monitor is in-memory only and is not a durable audit store.
    """

    _SEVERITIES = frozenset({"critical", "error", "warning", "info"})

    def __init__(self, event_service: CommandEventService, max_findings: int = 500) -> None:
        if not isinstance(event_service, CommandEventService):
            raise TypeError("event_service must be a CommandEventService")
        if isinstance(max_findings, bool) or not isinstance(max_findings, int) or max_findings < 1:
            raise ValueError("max_findings must be a positive integer")

        self._event_service = event_service
        self._max_findings = max_findings
        self._lock = RLock()
        self._total_events = 0
        self._malformed_events = 0
        self._severity_counts: Counter[str] = Counter()
        self._findings: dict[tuple[str, str], ExecutionDiagnostic] = {}
        self._closed = False
        self._event_service.dispatcher.subscribe(
            CommandEventType.EXECUTION_INTEGRITY_DIAGNOSTIC, self._on_event
        )

    def _on_event(self, event: CommandEvent) -> None:
        payload = event.payload
        execution_id = payload.get("execution_id")
        code = payload.get("code")
        severity = payload.get("severity")
        message = payload.get("message")
        sequence = payload.get("sequence")

        valid = (
            payload.get("diagnostic_type") == "execution_integrity"
            and isinstance(execution_id, str) and bool(execution_id.strip())
            and isinstance(code, str) and bool(code.strip())
            and isinstance(severity, str) and severity in self._SEVERITIES
            and isinstance(message, str) and bool(message.strip())
            and (sequence is None or (isinstance(sequence, int) and not isinstance(sequence, bool) and sequence >= 0))
        )
        with self._lock:
            if self._closed:
                return
            if not valid:
                self._malformed_events += 1
                return

            self._total_events += 1
            self._severity_counts[severity] += 1
            timestamp_iso = event.timestamp.isoformat()
            key = (execution_id, code)
            previous = self._findings.get(key)
            finding = ExecutionDiagnostic(
                event_id=event.event_id,
                execution_id=execution_id,
                code=code,
                severity=severity,
                message=message,
                timestamp_iso=timestamp_iso,
                sequence=sequence,
                occurrences=(previous.occurrences + 1) if previous else 1,
                first_seen_iso=(previous.first_seen_iso or previous.timestamp_iso) if previous else timestamp_iso,
            )
            self._findings[key] = finding
            # Keep the latest groups only; oldest by last-seen timestamp is evicted first.
            while len(self._findings) > self._max_findings:
                oldest_key = min(self._findings, key=lambda item: self._findings[item].timestamp_iso)
                del self._findings[oldest_key]

    def snapshot(self) -> ExecutionDiagnosticSnapshot:
        """Return a consistent immutable snapshot of current monitoring state."""
        with self._lock:
            findings = tuple(sorted(
                self._findings.values(),
                key=lambda item: (item.timestamp_iso, item.execution_id, item.code),
                reverse=True,
            ))
            return ExecutionDiagnosticSnapshot(
                total_events=self._total_events,
                malformed_events=self._malformed_events,
                severity_counts=tuple(sorted(self._severity_counts.items())),
                recent_findings=findings,
            )

    def summary_for_execution(self, execution_id: str) -> ExecutionDiagnosticSummary:
        """Summarize retained groups for an execution, never lifetime history."""
        if not isinstance(execution_id, str) or not execution_id.strip():
            raise ValueError("execution_id must be a non-empty string")
        with self._lock:
            findings = tuple(
                finding for (owner, _), finding in self._findings.items()
                if owner == execution_id
            )
            severity_counts = Counter(finding.severity for finding in findings)
            retained_occurrences = sum(finding.occurrences for finding in findings)
            repeated_groups = sum(finding.repeated for finding in findings)
            return ExecutionDiagnosticSummary(
                execution_id=execution_id,
                retained_groups=len(findings),
                repeated_groups=repeated_groups,
                retained_occurrences=retained_occurrences,
                repeated_occurrences=sum(max(0, finding.occurrences - 1) for finding in findings),
                severity_counts=tuple(sorted(severity_counts.items())),
            )

    def close(self) -> None:
        """Unsubscribe this monitor; subsequent events are not accumulated."""
        with self._lock:
            if self._closed:
                return
            self._closed = True
        self._event_service.dispatcher.unsubscribe(
            CommandEventType.EXECUTION_INTEGRITY_DIAGNOSTIC, self._on_event
        )

    def __enter__(self) -> ExecutionDiagnosticMonitor:
        return self

    def __exit__(self, exc_type, exc, traceback) -> None:
        self.close()
