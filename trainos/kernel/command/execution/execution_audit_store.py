from __future__ import annotations

import sqlite3
from pathlib import Path
from threading import RLock
from typing import Any

from .command_execution import CommandExecution
from .execution_progress import ExecutionProgress
from .execution_status import ExecutionStatus


class ExecutionAuditStore:
    """Append-only SQLite history of execution state transitions.

    Each save appends a transition record rather than overwriting the previous
    state. The database can be reopened after process restart to inspect history.
    This is an application audit log, not a tamper-proof safety log.
    """

    def __init__(self, database_path: str | Path) -> None:
        if not isinstance(database_path, (str, Path)) or not str(database_path).strip():
            raise ValueError("database_path must not be empty")
        self._database_path = str(database_path)
        self._lock = RLock()
        self._connection = sqlite3.connect(self._database_path, check_same_thread=False)
        self._connection.row_factory = sqlite3.Row
        with self._lock, self._connection:
            self._connection.execute("PRAGMA foreign_keys = ON")
            self._connection.execute(
                """CREATE TABLE IF NOT EXISTS execution_audit (
                    sequence INTEGER PRIMARY KEY AUTOINCREMENT,
                    execution_id TEXT NOT NULL,
                    command_id TEXT NOT NULL,
                    status TEXT NOT NULL,
                    attempts INTEGER NOT NULL,
                    max_attempts INTEGER NOT NULL,
                    completed INTEGER NOT NULL,
                    transition_reason TEXT,
                    recorded_at TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%fZ','now')),
                    UNIQUE(execution_id, status)
                )"""
            )
            # Migrate existing databases created before transition reasons were recorded.
            columns = {row["name"] for row in self._connection.execute("PRAGMA table_info(execution_audit)")}
            if "transition_reason" not in columns:
                self._connection.execute("ALTER TABLE execution_audit ADD COLUMN transition_reason TEXT")
            self._connection.execute(
                "CREATE INDEX IF NOT EXISTS idx_execution_audit_command ON execution_audit(command_id, sequence)"
            )
            self._connection.execute(
                """CREATE TABLE IF NOT EXISTS execution_reconciliation (
                    sequence INTEGER PRIMARY KEY AUTOINCREMENT,
                    execution_id TEXT NOT NULL,
                    decision TEXT NOT NULL,
                    reason TEXT NOT NULL,
                    evidence_reference TEXT,
                    recorded_at TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%fZ','now'))
                )"""
            )
            self._connection.execute(
                "CREATE INDEX IF NOT EXISTS idx_execution_reconciliation_id ON execution_reconciliation(execution_id, sequence)"
            )

    @property
    def database_path(self) -> str:
        return self._database_path

    def append(self, execution: CommandExecution) -> None:
        """Persist a state transition once; duplicate same-state writes are idempotent."""
        if not isinstance(execution, CommandExecution):
            raise TypeError("execution must be a CommandExecution")
        with self._lock, self._connection:
            existing = self._connection.execute(
                "SELECT command_id, attempts, max_attempts, completed FROM execution_audit "
                "WHERE execution_id = ? AND status = ?",
                (execution.execution_id, execution.status.value),
            ).fetchone()
            values = (
                execution.command_id,
                execution.progress.attempts,
                execution.progress.max_attempts,
                int(execution.progress.completed),
            )
            if existing is not None:
                if tuple(existing) != values:
                    raise ValueError("conflicting duplicate execution state")
                return
            latest = self._connection.execute(
                "SELECT command_id, status FROM execution_audit WHERE execution_id = ? "
                "ORDER BY sequence DESC LIMIT 1",
                (execution.execution_id,),
            ).fetchone()
            if latest is None:
                if execution.status.value != "created":
                    raise ValueError("first execution audit state must be created")
            else:
                if latest["command_id"] != execution.command_id:
                    raise ValueError("execution_id cannot be reused for another command")
                allowed_next = {
                    "created": {"running", "failed"},
                    "running": {"completed", "failed", "recovery_required"},
                    "completed": set(),
                    "failed": set(),
                    "recovery_required": set(),
                }
                if execution.status.value not in allowed_next[latest["status"]]:
                    raise ValueError(
                        f"invalid execution audit transition: {latest['status']} -> {execution.status.value}"
                    )
            self._connection.execute(
                "INSERT INTO execution_audit "
                "(execution_id, command_id, status, attempts, max_attempts, completed) "
                "VALUES (?, ?, ?, ?, ?, ?)",
                (execution.execution_id, execution.command_id, execution.status.value, *values[1:]),
            )

    def get_history(self, execution_id: str) -> tuple[dict[str, Any], ...]:
        if not isinstance(execution_id, str) or not execution_id.strip():
            raise ValueError("execution_id must not be empty")
        with self._lock:
            rows = self._connection.execute(
                "SELECT sequence, execution_id, command_id, status, attempts, max_attempts, "
                "completed, transition_reason, recorded_at FROM execution_audit WHERE execution_id = ? ORDER BY sequence",
                (execution_id,),
            ).fetchall()
        return tuple(dict(row) for row in rows)

    def get_command_history(self, command_id: str) -> tuple[dict[str, Any], ...]:
        if not isinstance(command_id, str) or not command_id.strip():
            raise ValueError("command_id must not be empty")
        with self._lock:
            rows = self._connection.execute(
                "SELECT sequence, execution_id, command_id, status, attempts, max_attempts, "
                "completed, transition_reason, recorded_at FROM execution_audit WHERE command_id = ? ORDER BY sequence",
                (command_id,),
            ).fetchall()
        return tuple(dict(row) for row in rows)

    def recover_incomplete_executions(self) -> tuple[CommandExecution, ...]:
        """Mark executions left RUNNING by a prior process as requiring reconciliation.

        This is deliberately not an automatic retry: a previous handler may have
        completed an external side effect before the process stopped.
        """
        recovered: list[CommandExecution] = []
        with self._lock:
            latest_rows = self._connection.execute(
                """SELECT a.execution_id, a.command_id, a.status, a.attempts,
                          a.max_attempts, a.completed
                   FROM execution_audit AS a
                   JOIN (SELECT execution_id, MAX(sequence) AS sequence
                         FROM execution_audit GROUP BY execution_id) AS latest
                     ON latest.execution_id = a.execution_id AND latest.sequence = a.sequence
                   WHERE a.status = 'running'
                   ORDER BY a.sequence"""
            ).fetchall()
            for row in latest_rows:
                execution = CommandExecution(
                    execution_id=row["execution_id"],
                    command_id=row["command_id"],
                    progress=ExecutionProgress(
                        attempts=row["attempts"],
                        max_attempts=row["max_attempts"],
                        completed=bool(row["completed"]),
                    ),
                    status=ExecutionStatus.RECOVERY_REQUIRED,
                )
                self.append(execution)
                recovered.append(execution)
        return tuple(recovered)

    def reconcile_recovery(
        self,
        execution_id: str,
        decision: str,
        reason: str,
        evidence_reference: str | None = None,
    ) -> str:
        """Record an explicit recovery decision, never infer an outcome automatically.

        ``manual_investigation`` records a review request while keeping the execution
        in ``recovery_required``. ``confirmed_completed`` and ``confirmed_failed``
        require a non-empty reason and append the corresponding terminal audit state.
        A final decision can only be made once, while manual-investigation entries
        may be added repeatedly until a final decision is recorded.
        """
        if not isinstance(execution_id, str) or not execution_id.strip():
            raise ValueError("execution_id must not be empty")
        allowed = {"confirmed_completed", "confirmed_failed", "manual_investigation"}
        if not isinstance(decision, str) or decision not in allowed:
            raise ValueError(f"decision must be one of {sorted(allowed)}")
        if not isinstance(reason, str) or not reason.strip():
            raise ValueError("reason must not be empty")
        if evidence_reference is not None and (
            not isinstance(evidence_reference, str) or not evidence_reference.strip()
        ):
            raise ValueError("evidence_reference must be a non-empty string when provided")

        with self._lock, self._connection:
            latest = self._connection.execute(
                "SELECT sequence, command_id, status, attempts, max_attempts, completed "
                "FROM execution_audit WHERE execution_id = ? ORDER BY sequence DESC LIMIT 1",
                (execution_id,),
            ).fetchone()
            if latest is None:
                raise ValueError("unknown execution_id")
            if latest["status"] != ExecutionStatus.RECOVERY_REQUIRED.value:
                raise ValueError("only recovery_required executions can be reconciled")

            self._connection.execute(
                "INSERT INTO execution_reconciliation "
                "(execution_id, decision, reason, evidence_reference) VALUES (?, ?, ?, ?)",
                (execution_id, decision, reason.strip(), evidence_reference.strip() if evidence_reference else None),
            )
            if decision == "manual_investigation":
                return latest["status"]

            final_status = (
                ExecutionStatus.COMPLETED.value
                if decision == "confirmed_completed"
                else ExecutionStatus.FAILED.value
            )
            completed = int(decision == "confirmed_completed")
            self._connection.execute(
                "INSERT INTO execution_audit "
                "(execution_id, command_id, status, attempts, max_attempts, completed, transition_reason) "
                "VALUES (?, ?, ?, ?, ?, ?, ?)",
                (
                    execution_id, latest["command_id"], final_status,
                    latest["attempts"], latest["max_attempts"], completed, reason.strip(),
                ),
            )
            return final_status

    def get_reconciliation_history(self, execution_id: str) -> tuple[dict[str, Any], ...]:
        """Return immutable-by-convention reconciliation records in append order."""
        if not isinstance(execution_id, str) or not execution_id.strip():
            raise ValueError("execution_id must not be empty")
        with self._lock:
            rows = self._connection.execute(
                "SELECT sequence, execution_id, decision, reason, evidence_reference, recorded_at "
                "FROM execution_reconciliation WHERE execution_id = ? ORDER BY sequence",
                (execution_id,),
            ).fetchall()
        return tuple(dict(row) for row in rows)

    def verify_integrity(self) -> tuple[dict[str, Any], ...]:
        """Read-only consistency check for execution and reconciliation history.

        Findings are diagnostics, not repairs. A clean result is an empty tuple.
        This detects logical inconsistencies in the application ledger; it does
        not prove that the SQLite file has not been maliciously modified.
        """
        findings: list[dict[str, Any]] = []
        allowed_statuses = {status.value for status in ExecutionStatus}
        allowed_next = {
            "created": {"running", "failed"},
            "running": {"completed", "failed", "recovery_required"},
            "completed": set(),
            "failed": set(),
            "recovery_required": {"completed", "failed"},
        }

        def report(code: str, execution_id: str, message: str, sequence: int | None = None) -> None:
            finding: dict[str, Any] = {
                "code": code,
                "execution_id": execution_id,
                "message": message,
            }
            if sequence is not None:
                finding["sequence"] = sequence
            findings.append(finding)

        with self._lock:
            audit_rows = self._connection.execute(
                "SELECT sequence, execution_id, command_id, status, attempts, max_attempts, "
                "completed, transition_reason FROM execution_audit ORDER BY execution_id, sequence"
            ).fetchall()
            reconciliation_rows = self._connection.execute(
                "SELECT sequence, execution_id, decision, reason, evidence_reference "
                "FROM execution_reconciliation ORDER BY execution_id, sequence"
            ).fetchall()

        by_execution: dict[str, list[sqlite3.Row]] = {}
        for row in audit_rows:
            by_execution.setdefault(str(row["execution_id"]), []).append(row)

        for execution_id, rows in by_execution.items():
            previous = None
            for row in rows:
                sequence = int(row["sequence"])
                status = str(row["status"])
                if status not in allowed_statuses:
                    report("unknown_status", execution_id, f"Unknown execution status: {status}", sequence)
                attempts, max_attempts = row["attempts"], row["max_attempts"]
                if not isinstance(attempts, int) or attempts < 0:
                    report("invalid_attempts", execution_id, "attempts must be a non-negative integer", sequence)
                if not isinstance(max_attempts, int) or max_attempts < 1:
                    report("invalid_max_attempts", execution_id, "max_attempts must be a positive integer", sequence)
                if isinstance(attempts, int) and isinstance(max_attempts, int) and (attempts < 0 or max_attempts < 1 or attempts > max_attempts):
                    report("invalid_progress", execution_id, "attempt counters violate ExecutionProgress invariants", sequence)
                completed = row["completed"]
                if completed not in (0, 1):
                    report("invalid_completed_flag", execution_id, "completed must be stored as 0 or 1", sequence)
                if status == "completed" and completed != 1:
                    report("completed_flag_mismatch", execution_id, "completed status must have completed=1", sequence)
                if status in {"failed", "recovery_required", "created", "running"} and completed == 1:
                    report("completed_flag_mismatch", execution_id, f"{status} status must not have completed=1", sequence)
                if previous is None:
                    if status != "created":
                        report("missing_initial_state", execution_id, "First audit state must be created", sequence)
                else:
                    if row["command_id"] != previous["command_id"]:
                        report("command_id_changed", execution_id, "command_id changed within one execution", sequence)
                    prior_status = str(previous["status"])
                    if status not in allowed_next.get(prior_status, set()):
                        report("invalid_transition", execution_id, f"Invalid transition: {prior_status} -> {status}", sequence)
                    if prior_status == "recovery_required" and status in {"completed", "failed"}:
                        # Final recovery transitions must have a matching explicit decision.
                        expected = "confirmed_completed" if status == "completed" else "confirmed_failed"
                        matching = any(
                            rec["execution_id"] == execution_id and rec["decision"] == expected
                            for rec in reconciliation_rows
                        )
                        if not matching:
                            report("missing_reconciliation", execution_id, f"{status} after recovery_required lacks {expected}", sequence)
                previous = row

        for row in reconciliation_rows:
            execution_id = str(row["execution_id"])
            decision = str(row["decision"])
            if decision not in {"manual_investigation", "confirmed_completed", "confirmed_failed"}:
                report("unknown_reconciliation_decision", execution_id, f"Unknown reconciliation decision: {decision}", int(row["sequence"]))
            if not isinstance(row["reason"], str) or not row["reason"].strip():
                report("missing_reconciliation_reason", execution_id, "Reconciliation reason must not be empty", int(row["sequence"]))
            states = by_execution.get(execution_id, [])
            if not any(str(state["status"]) == "recovery_required" for state in states):
                report("orphan_reconciliation", execution_id, "Reconciliation record has no recovery_required state", int(row["sequence"]))
            if decision == "confirmed_completed" and not any(str(state["status"]) == "completed" for state in states):
                report("decision_status_mismatch", execution_id, "confirmed_completed has no completed audit state", int(row["sequence"]))
            if decision == "confirmed_failed" and not any(str(state["status"]) == "failed" for state in states):
                report("decision_status_mismatch", execution_id, "confirmed_failed has no failed audit state", int(row["sequence"]))

        findings.sort(key=lambda item: (item["execution_id"], item.get("sequence", -1), item["code"]))
        return tuple(findings)

    def get_latest_status(self, execution_id: str) -> str | None:
        """Return the latest persisted status, or None for an unknown execution."""
        if not isinstance(execution_id, str) or not execution_id.strip():
            raise ValueError("execution_id must not be empty")
        with self._lock:
            row = self._connection.execute(
                "SELECT status FROM execution_audit WHERE execution_id = ? ORDER BY sequence DESC LIMIT 1",
                (execution_id,),
            ).fetchone()
        return None if row is None else str(row["status"])

    def close(self) -> None:
        with self._lock:
            self._connection.close()

    def __enter__(self) -> "ExecutionAuditStore":
        return self

    def __exit__(self, exc_type: object, exc: object, traceback: object) -> None:
        self.close()
