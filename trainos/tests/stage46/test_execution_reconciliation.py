import sqlite3

import pytest

from kernel.command.execution.command_execution import CommandExecution
from kernel.command.execution.execution_audit_store import ExecutionAuditStore
from kernel.command.execution.execution_progress import ExecutionProgress
from kernel.command.execution.execution_status import ExecutionStatus


def _record(status, execution_id="exec-reconcile"):
    return CommandExecution(
        execution_id=execution_id,
        command_id=f"cmd-{execution_id}",
        progress=ExecutionProgress(attempts=0, max_attempts=1, completed=False),
        status=status,
    )


def _recovery_required(store, execution_id="exec-reconcile"):
    store.append(_record(ExecutionStatus.CREATED, execution_id))
    store.append(_record(ExecutionStatus.RUNNING, execution_id))
    store.recover_incomplete_executions()


def test_manual_investigation_is_logged_without_falsifying_execution_outcome(tmp_path):
    with ExecutionAuditStore(tmp_path / "reconcile.sqlite3") as store:
        _recovery_required(store)
        status = store.reconcile_recovery(
            "exec-reconcile", "manual_investigation", "External system outcome not yet verified"
        )
        assert status == "recovery_required"
        assert store.get_latest_status("exec-reconcile") == "recovery_required"
        records = store.get_reconciliation_history("exec-reconcile")
        assert len(records) == 1
        assert records[0]["decision"] == "manual_investigation"
        assert records[0]["reason"] == "External system outcome not yet verified"


def test_confirmed_completion_appends_terminal_status_and_reason(tmp_path):
    with ExecutionAuditStore(tmp_path / "complete.sqlite3") as store:
        _recovery_required(store)
        status = store.reconcile_recovery(
            "exec-reconcile", "confirmed_completed", "Verified by downstream transaction ID", "txn-123"
        )
        assert status == "completed"
        history = store.get_history("exec-reconcile")
        assert [row["status"] for row in history] == [
            "created", "running", "recovery_required", "completed"
        ]
        assert history[-1]["completed"] == 1
        assert history[-1]["transition_reason"] == "Verified by downstream transaction ID"
        assert store.get_reconciliation_history("exec-reconcile")[-1]["evidence_reference"] == "txn-123"


def test_confirmed_failure_appends_failed_status(tmp_path):
    with ExecutionAuditStore(tmp_path / "failed.sqlite3") as store:
        _recovery_required(store)
        assert store.reconcile_recovery(
            "exec-reconcile", "confirmed_failed", "External system confirms rejection"
        ) == "failed"
        assert store.get_latest_status("exec-reconcile") == "failed"
        assert store.get_history("exec-reconcile")[-1]["completed"] == 0


def test_final_decision_cannot_be_repeated_or_reversed(tmp_path):
    with ExecutionAuditStore(tmp_path / "single-final.sqlite3") as store:
        _recovery_required(store)
        store.reconcile_recovery("exec-reconcile", "confirmed_failed", "Verified rejection")
        with pytest.raises(ValueError, match="only recovery_required"):
            store.reconcile_recovery("exec-reconcile", "confirmed_completed", "Contradictory evidence")
        assert store.get_latest_status("exec-reconcile") == "failed"


def test_invalid_decisions_reasons_and_unknown_ids_are_rejected(tmp_path):
    with ExecutionAuditStore(tmp_path / "validation.sqlite3") as store:
        _recovery_required(store)
        with pytest.raises(ValueError, match="decision must be"):
            store.reconcile_recovery("exec-reconcile", "completed", "some reason")
        with pytest.raises(ValueError, match="reason must not be empty"):
            store.reconcile_recovery("exec-reconcile", "confirmed_failed", " ")
        with pytest.raises(ValueError, match="unknown execution_id"):
            store.reconcile_recovery("unknown", "manual_investigation", "Investigate")
        with pytest.raises(ValueError, match="evidence_reference"):
            store.reconcile_recovery(
                "exec-reconcile", "manual_investigation", "Investigate", "  "
            )


def test_reconciliation_history_persists_after_reopen(tmp_path):
    path = tmp_path / "reopen.sqlite3"
    with ExecutionAuditStore(path) as store:
        _recovery_required(store)
        store.reconcile_recovery("exec-reconcile", "manual_investigation", "Need operator review")
    with ExecutionAuditStore(path) as reopened:
        history = reopened.get_reconciliation_history("exec-reconcile")
        assert len(history) == 1
        assert history[0]["reason"] == "Need operator review"
        assert reopened.get_latest_status("exec-reconcile") == "recovery_required"


def test_old_database_is_migrated_with_transition_reason_column(tmp_path):
    path = tmp_path / "legacy.sqlite3"
    connection = sqlite3.connect(path)
    connection.execute(
        """CREATE TABLE execution_audit (
            sequence INTEGER PRIMARY KEY AUTOINCREMENT,
            execution_id TEXT NOT NULL,
            command_id TEXT NOT NULL,
            status TEXT NOT NULL,
            attempts INTEGER NOT NULL,
            max_attempts INTEGER NOT NULL,
            completed INTEGER NOT NULL,
            recorded_at TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%fZ','now')),
            UNIQUE(execution_id, status)
        )"""
    )
    connection.commit()
    connection.close()
    with ExecutionAuditStore(path) as store:
        columns = {row["name"] for row in store._connection.execute("PRAGMA table_info(execution_audit)")}
        assert "transition_reason" in columns
        _recovery_required(store)
        store.reconcile_recovery("exec-reconcile", "confirmed_failed", "Verified failure")
        assert store.get_history("exec-reconcile")[-1]["transition_reason"] == "Verified failure"
