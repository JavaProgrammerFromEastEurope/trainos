from kernel.command.execution.command_execution import CommandExecution
from kernel.command.execution.execution_audit_store import ExecutionAuditStore
from kernel.command.execution.execution_progress import ExecutionProgress
from kernel.command.execution.execution_status import ExecutionStatus


def _execution(status: ExecutionStatus, execution_id: str = "exec-restart") -> CommandExecution:
    return CommandExecution(
        execution_id=execution_id,
        command_id=f"cmd-{execution_id}",
        progress=ExecutionProgress(attempts=0, max_attempts=1, completed=False),
        status=status,
    )


def test_recovery_marks_running_execution_without_retrying(tmp_path):
    path = tmp_path / "recovery.sqlite3"
    with ExecutionAuditStore(path) as store:
        store.append(_execution(ExecutionStatus.CREATED))
        store.append(_execution(ExecutionStatus.RUNNING))

    with ExecutionAuditStore(path) as restarted_store:
        recovered = restarted_store.recover_incomplete_executions()
        assert len(recovered) == 1
        assert recovered[0].status is ExecutionStatus.RECOVERY_REQUIRED
        assert restarted_store.get_latest_status("exec-restart") == "recovery_required"
        assert [r["status"] for r in restarted_store.get_history("exec-restart")] == [
            "created", "running", "recovery_required"
        ]


def test_recovery_does_not_touch_terminal_executions(tmp_path):
    store = ExecutionAuditStore(tmp_path / "terminal.sqlite3")
    store.append(_execution(ExecutionStatus.CREATED, "exec-done"))
    store.append(_execution(ExecutionStatus.RUNNING, "exec-done"))
    store.append(_execution(ExecutionStatus.COMPLETED, "exec-done"))
    assert store.recover_incomplete_executions() == ()
    assert store.get_latest_status("exec-done") == "completed"
    store.close()


def test_recovery_is_idempotent(tmp_path):
    store = ExecutionAuditStore(tmp_path / "idempotent.sqlite3")
    store.append(_execution(ExecutionStatus.CREATED))
    store.append(_execution(ExecutionStatus.RUNNING))
    assert len(store.recover_incomplete_executions()) == 1
    assert store.recover_incomplete_executions() == ()
    assert [r["status"] for r in store.get_history("exec-restart")] == [
        "created", "running", "recovery_required"
    ]
    store.close()


def test_recovery_keeps_other_running_executions_independent(tmp_path):
    store = ExecutionAuditStore(tmp_path / "multiple.sqlite3")
    for execution_id in ("exec-a", "exec-b"):
        store.append(_execution(ExecutionStatus.CREATED, execution_id))
        store.append(_execution(ExecutionStatus.RUNNING, execution_id))
    recovered = store.recover_incomplete_executions()
    assert {item.execution_id for item in recovered} == {"exec-a", "exec-b"}
    assert store.get_latest_status("exec-a") == "recovery_required"
    assert store.get_latest_status("exec-b") == "recovery_required"
    store.close()


def test_recovery_required_is_terminal_for_ordinary_transitions(tmp_path):
    store = ExecutionAuditStore(tmp_path / "terminal-recovery.sqlite3")
    store.append(_execution(ExecutionStatus.CREATED))
    store.append(_execution(ExecutionStatus.RUNNING))
    store.recover_incomplete_executions()
    invalid = _execution(ExecutionStatus.COMPLETED)
    try:
        store.append(invalid)
    except ValueError as exc:
        assert "invalid execution audit transition" in str(exc)
    else:
        raise AssertionError("recovery-required execution must not transition directly to completed")
    store.close()
