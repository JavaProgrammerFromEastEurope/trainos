import pytest

from kernel.command.bus.command_dispatcher import CommandDispatcher
from kernel.command.command.command import Command
from kernel.command.command.command_priority import CommandPriority
from kernel.command.execution.execution_registry import ExecutionRegistry
from kernel.command.execution.execution_status import ExecutionStatus
from kernel.command.events import CommandEventService, CommandEventType
from kernel.command.handler.command_handler import CommandHandler
from kernel.command.handler.handler_registry import HandlerRegistry


def make_command(name="inspect", command_id="cmd-43"):
    return Command(command_id, name, CommandPriority.NORMAL)


def test_success_dispatch_records_completed_execution_and_lifecycle_events():
    events = CommandEventService()
    registry = HandlerRegistry()
    registry.register("handler-1", CommandHandler("handler-1", "inspect", executor=lambda cmd: {"id": cmd.command_id}))
    executions = ExecutionRegistry()
    result = CommandDispatcher(registry, execution_registry=executions, event_service=events).dispatch(make_command())

    assert result.success
    assert result.execution_id
    assert result.execution_status is ExecutionStatus.COMPLETED
    saved = executions.get(result.execution_id)
    assert saved.status is ExecutionStatus.COMPLETED
    assert [e.event_type for e in events.registry.get_events("cmd-43")] == [
        CommandEventType.COMMAND_CREATED,
        CommandEventType.COMMAND_STARTED,
        CommandEventType.COMMAND_COMPLETED,
    ]


def test_routing_failure_records_failed_execution_and_failure_event():
    events = CommandEventService()
    executions = ExecutionRegistry()
    result = CommandDispatcher(HandlerRegistry(), execution_registry=executions, event_service=events).dispatch(make_command())

    assert not result.success
    assert result.execution_status is ExecutionStatus.FAILED
    assert executions.get(result.execution_id).status is ExecutionStatus.FAILED
    assert [e.event_type for e in events.registry.get_events("cmd-43")][-1] is CommandEventType.COMMAND_FAILED


def test_executor_failure_records_failed_execution_and_failure_event():
    events = CommandEventService()
    registry = HandlerRegistry()
    def fail(_command):
        raise RuntimeError("executor broke")
    registry.register("handler-1", CommandHandler("handler-1", "inspect", executor=fail))
    result = CommandDispatcher(registry, event_service=events).dispatch(make_command())

    assert not result.success
    assert result.execution_status is ExecutionStatus.FAILED
    assert "executor broke" in result.error
    assert events.registry.get_latest("cmd-43").event_type is CommandEventType.COMMAND_FAILED


def test_event_observer_exception_does_not_interrupt_other_observers_or_execution():
    events = CommandEventService()
    seen = []
    def broken(_event):
        raise RuntimeError("observer failed")
    events.dispatcher.subscribe(CommandEventType.COMMAND_STARTED, broken)
    events.dispatcher.subscribe(CommandEventType.COMMAND_STARTED, lambda event: seen.append(event.command_id))
    registry = HandlerRegistry()
    registry.register("handler-1", CommandHandler("handler-1", "inspect", executor=lambda _cmd: "ok"))

    result = CommandDispatcher(registry, event_service=events).dispatch(make_command())
    assert result.success
    assert seen == ["cmd-43"]
    assert len(events.dispatcher.last_errors) == 0  # later events have no failing observers


def test_execution_engine_rejects_invalid_state_transition():
    from kernel.command.execution.command_execution import CommandExecution
    from kernel.command.execution.execution_engine import ExecutionEngine
    from kernel.command.execution.execution_progress import ExecutionProgress

    engine = ExecutionEngine()
    created = CommandExecution("exec", "cmd", ExecutionProgress(0, 1, False))
    with pytest.raises(ValueError, match="cannot complete"):
        engine.complete(created)


def test_event_dispatcher_exposes_observer_errors():
    events = CommandEventService()
    def broken(_event):
        raise RuntimeError("observer failed")
    events.dispatcher.subscribe(CommandEventType.COMMAND_CREATED, broken)
    events.publish("cmd-errors", CommandEventType.COMMAND_CREATED, {})
    assert len(events.dispatcher.last_errors) == 1
    assert isinstance(events.dispatcher.last_errors[0][1], RuntimeError)
