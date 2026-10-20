from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Protocol

from .command_event import CommandEvent
from .event_service import CommandEventService
from .event_type import CommandEventType


class IntegrityVerifier(Protocol):
    def verify_integrity(self) -> tuple[dict[str, Any], ...]: ...


@dataclass(frozen=True, slots=True)
class IntegrityEventPublishResult:
    """Best-effort publication summary; it never changes the audit ledger."""

    findings_count: int
    published_events: tuple[CommandEvent, ...]
    publish_failures: tuple[dict[str, str], ...]
    subscriber_failures: tuple[dict[str, str], ...]

    @property
    def successful(self) -> bool:
        return not self.publish_failures and not self.subscriber_failures


class ExecutionIntegrityEventAdapter:
    """Publish read-only execution-integrity findings through command events.

    Event delivery is best-effort. Failures are reported to the caller, and no
    finding triggers a repair or a change to execution status.
    """

    _CRITICAL_CODES = frozenset({
        "unknown_status",
        "invalid_transition",
        "command_id_changed",
        "missing_initial_state",
        "missing_reconciliation",
        "decision_status_mismatch",
        "unknown_reconciliation_decision",
    })

    def __init__(self, event_service: CommandEventService) -> None:
        if not isinstance(event_service, CommandEventService):
            raise TypeError("event_service must be a CommandEventService")
        self._event_service = event_service

    def verify_and_publish(self, store: IntegrityVerifier) -> IntegrityEventPublishResult:
        """Verify the store, then publish one diagnostic event per finding."""
        verify = getattr(store, "verify_integrity", None)
        if not callable(verify):
            raise TypeError("store must provide verify_integrity()")
        findings = verify()
        if not isinstance(findings, (tuple, list)):
            raise TypeError("verify_integrity() must return a tuple or list")
        return self.publish_findings(findings)

    def publish_findings(
        self, findings: tuple[dict[str, Any], ...] | list[dict[str, Any]]
    ) -> IntegrityEventPublishResult:
        if not isinstance(findings, (tuple, list)):
            raise TypeError("findings must be a tuple or list")

        published: list[CommandEvent] = []
        publish_failures: list[dict[str, str]] = []
        subscriber_failures: list[dict[str, str]] = []

        for index, finding in enumerate(findings):
            if not isinstance(finding, dict):
                raise TypeError(f"finding at index {index} must be a dict")
            execution_id = finding.get("execution_id")
            code = finding.get("code")
            message = finding.get("message")
            if not all(isinstance(value, str) and value.strip() for value in (execution_id, code, message)):
                raise ValueError(f"finding at index {index} requires execution_id, code and message")

            severity = "critical" if code in self._CRITICAL_CODES else "error"
            payload = {
                "diagnostic_type": "execution_integrity",
                "execution_id": execution_id,
                "code": code,
                "severity": severity,
                "message": message,
            }
            if "sequence" in finding:
                payload["sequence"] = finding["sequence"]

            try:
                event = self._event_service.publish(
                    command_id=execution_id,
                    event_type=CommandEventType.EXECUTION_INTEGRITY_DIAGNOSTIC,
                    payload=payload,
                )
                published.append(event)
            except Exception as exc:
                publish_failures.append({
                    "execution_id": execution_id,
                    "code": code,
                    "error": f"{type(exc).__name__}: {exc}",
                })
                continue

            # EventDispatcher isolates observer errors; expose them here instead
            # of claiming that all subscribers received the event successfully.
            for handler, exc in self._event_service.dispatcher.last_errors:
                subscriber_failures.append({
                    "event_id": event.event_id,
                    "execution_id": execution_id,
                    "code": code,
                    "handler": getattr(handler, "__qualname__", repr(handler)),
                    "error": f"{type(exc).__name__}: {exc}",
                })

        return IntegrityEventPublishResult(
            findings_count=len(findings),
            published_events=tuple(published),
            publish_failures=tuple(publish_failures),
            subscriber_failures=tuple(subscriber_failures),
        )
