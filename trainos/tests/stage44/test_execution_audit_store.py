import pytest

from kernel.command.bus.command_dispatcher import CommandDispatcher
from kernel.command.command.command import Command
from kernel.command.command.command_priority import CommandPriority
from kernel.command.execution.command_execution import CommandExecution
from kernel.command.execution.execution_audit_store import ExecutionAuditStore
from kernel.command.execution.execution_progress import ExecutionProgress
from kernel.command.execution.execution_status import ExecutionStatus
from kernel.command.handler.command_handler import CommandHandler
from kernel.command.handler.handler_registry import HandlerRegistry


def execution(status=ExecutionStatus.CREATED):
    return CommandExecution(
        "exec-1", "cmd-1", ExecutionProgress(attempts=0, max_attempts=1, completed=False), status
    )


def test_audit_store_persists_append_only_history_across_reopen(tmp_path):
    path = tmp_path / "audit.sqlite3"
    store = ExecutionAuditStore(path)
    store.append(execution())
    store.append(CommandExecution("exec-1", "cmd-1", execution().progress, ExecutionStatus.RUNNING))
    store.close()

    reopened = ExecutionAuditStore(path)
    history = reopened.get_history("exec-1")
    assert [entry["status"] for entry in history] == ["created", "running"]
    assert all(entry["command_id"] == "cmd-1" for entry in history)
    reopened.close()


def test_duplicate_same_state_is_idempotent_but_conflict_is_rejected(tmp_path):
    store = ExecutionAuditStore(tmp_path / "audit.sqlite3")
    record = execution()
    store.append(record)
    store.append(record)
    assert len(store.get_history("exec-1")) == 1
    conflict = CommandExecution(
        "exec-1", "cmd-1", ExecutionProgress(1, 1, False), ExecutionStatus.CREATED
    )
    with pytest.raises(ValueError, match="conflicting duplicate"):
        store.append(conflict)
    store.close()


def test_dispatcher_writes_all_lifecycle_states_to_audit_store(tmp_path):
    store = ExecutionAuditStore(tmp_path / "audit.sqlite3")
    handlers = HandlerRegistry()
    handlers.register("h1", CommandHandler("h1", "inspect", executor=lambda command: "ok"))
    command = Command("cmd-44", "inspect", CommandPriority.NORMAL)
    result = CommandDispatcher(handlers, audit_store=store).dispatch(command)

    assert result.success
    history = store.get_history(result.execution_id)
    assert [row["status"] for row in history] == [
        "created", "running", "completed"
    ]
    store.close()


def test_dispatcher_persists_failure_transition(tmp_path):
    store = ExecutionAuditStore(tmp_path / "audit.sqlite3")
    command = Command("cmd-45", "missing", CommandPriority.NORMAL)
    result = CommandDispatcher(HandlerRegistry(), audit_store=store).dispatch(command)
    assert not result.success
    assert [row["status"] for row in store.get_history(result.execution_id)] == [
        "created", "running", "failed"
    ]
    assert store.get_command_history("cmd-45")[-1]["status"] == "failed"
    store.close()


def test_invalid_inputs_are_rejected(tmp_path):
    store = ExecutionAuditStore(tmp_path / "audit.sqlite3")
    with pytest.raises(TypeError, match="CommandExecution"):
        store.append(object())
    with pytest.raises(ValueError, match="execution_id"):
        store.get_history(" ")
    store.close()


def test_audit_store_rejects_out_of_order_transitions_and_reused_ids(tmp_path):
    store = ExecutionAuditStore(tmp_path / "audit.sqlite3")
    with pytest.raises(ValueError, match="first execution audit state must be created"):
        store.append(CommandExecution(
            "exec-x", "cmd-x", ExecutionProgress(0, 1, False), ExecutionStatus.RUNNING
        ))
    store.append(execution())
    with pytest.raises(ValueError, match="cannot be reused"):
        store.append(CommandExecution(
            "exec-1", "another-command", execution().progress, ExecutionStatus.RUNNING
        ))
    with pytest.raises(ValueError, match="invalid execution audit transition"):
        store.append(CommandExecution(
            "exec-1", "cmd-1", execution().progress, ExecutionStatus.COMPLETED
        ))
    store.close()
