import sqlite3

from kernel.command.execution.command_execution import CommandExecution
from kernel.command.execution.execution_audit_store import ExecutionAuditStore
from kernel.command.execution.execution_progress import ExecutionProgress
from kernel.command.execution.execution_status import ExecutionStatus


def record(status, execution_id="exec-integrity", command_id="cmd-integrity", completed=False):
    return CommandExecution(
        execution_id=execution_id,
        command_id=command_id,
        progress=ExecutionProgress(attempts=0, max_attempts=1, completed=completed),
        status=status,
    )


def make_recovery(store, execution_id="exec-integrity"):
    store.append(record(ExecutionStatus.CREATED, execution_id))
    store.append(record(ExecutionStatus.RUNNING, execution_id))
    store.recover_incomplete_executions()


def test_clean_history_has_no_integrity_findings(tmp_path):
    with ExecutionAuditStore(tmp_path / "clean.sqlite3") as store:
        store.append(record(ExecutionStatus.CREATED))
        store.append(record(ExecutionStatus.RUNNING))
        store.append(record(ExecutionStatus.COMPLETED, completed=True))
        assert store.verify_integrity() == ()


def test_reconciled_recovery_history_is_consistent(tmp_path):
    with ExecutionAuditStore(tmp_path / "reconciled.sqlite3") as store:
        make_recovery(store)
        store.reconcile_recovery("exec-integrity", "confirmed_failed", "Verified downstream rejection")
        assert store.verify_integrity() == ()


def test_integrity_check_reports_invalid_transition_without_repairing(tmp_path):
    path = tmp_path / "tampered.sqlite3"
    with ExecutionAuditStore(path) as store:
        store.append(record(ExecutionStatus.CREATED))
        store.append(record(ExecutionStatus.RUNNING))
        store._connection.execute(
            "UPDATE execution_audit SET status='completed', completed=1 WHERE execution_id=? AND status='running'",
            ("exec-integrity",),
        )
        before = store.get_history("exec-integrity")
        findings = store.verify_integrity()
        after = store.get_history("exec-integrity")
        assert any(item["code"] == "invalid_transition" for item in findings)
        assert before == after


def test_integrity_check_detects_command_id_reuse_and_invalid_progress(tmp_path):
    with ExecutionAuditStore(tmp_path / "metadata.sqlite3") as store:
        store.append(record(ExecutionStatus.CREATED))
        store.append(record(ExecutionStatus.RUNNING))
        store._connection.execute(
            "UPDATE execution_audit SET command_id='different-command', attempts=2 WHERE execution_id=? AND status='running'",
            ("exec-integrity",),
        )
        codes = {item["code"] for item in store.verify_integrity()}
        assert "command_id_changed" in codes
        assert "invalid_progress" in codes


def test_integrity_check_detects_reconciliation_without_recovery_state(tmp_path):
    with ExecutionAuditStore(tmp_path / "orphan.sqlite3") as store:
        store.append(record(ExecutionStatus.CREATED))
        store._connection.execute(
            "INSERT INTO execution_reconciliation (execution_id, decision, reason) VALUES (?, ?, ?)",
            ("exec-integrity", "manual_investigation", "Injected inconsistent record"),
        )
        assert any(item["code"] == "orphan_reconciliation" for item in store.verify_integrity())
