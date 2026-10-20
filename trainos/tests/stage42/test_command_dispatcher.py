import pytest

from kernel.command.bus.command_dispatcher import CommandDispatcher
from kernel.command.command.command import Command
from kernel.command.command.command_priority import CommandPriority
from kernel.command.handler.command_handler import CommandHandler
from kernel.command.handler.handler_registry import HandlerRegistry


def make_command(name="inspect"):
    return Command("cmd-42", name, CommandPriority.NORMAL)


def registry_with(handler):
    registry = HandlerRegistry()
    registry.register(handler.handler_id, handler)
    return registry


def test_dispatch_routes_and_executes_handler_once_and_returns_output():
    calls = []
    handler = CommandHandler(
        "handler-1", "inspect", executor=lambda command: calls.append(command.command_id) or {"ok": True}
    )
    result = CommandDispatcher(registry_with(handler)).dispatch(make_command())

    assert result.success is True
    assert result.phase == "completed"
    assert result.command_id == "cmd-42"
    assert result.handler_id == "handler-1"
    assert result.output == {"ok": True}
    assert result.error is None
    assert calls == ["cmd-42"]


def test_dispatch_missing_handler_reports_routing_failure_without_execution():
    result = CommandDispatcher(HandlerRegistry()).dispatch(make_command())

    assert result.success is False
    assert result.phase == "routing"
    assert result.handler_id is None
    assert "No handler registered" in result.error


def test_dispatch_metadata_only_handler_fails_closed():
    result = CommandDispatcher(
        registry_with(CommandHandler("handler-1", "inspect"))
    ).dispatch(make_command())

    assert result.success is False
    assert result.phase == "routing"
    assert result.handler_id == "handler-1"
    assert "no executor" in result.error


def test_dispatch_executor_exception_is_returned_as_execution_failure():
    def fail(_command):
        raise RuntimeError("device unavailable")

    result = CommandDispatcher(
        registry_with(CommandHandler("handler-1", "inspect", executor=fail))
    ).dispatch(make_command())

    assert result.success is False
    assert result.phase == "execution"
    assert result.handler_id == "handler-1"
    assert "RuntimeError: device unavailable" == result.error
    assert result.output is None


def test_dispatch_does_not_execute_ambiguous_handler_names():
    calls = []
    registry = HandlerRegistry()
    registry.register("h1", CommandHandler("h1", "inspect", executor=lambda cmd: calls.append("h1")))
    registry.register("h2", CommandHandler("h2", "inspect", executor=lambda cmd: calls.append("h2")))

    result = CommandDispatcher(registry).dispatch(make_command())

    assert result.success is False
    assert result.phase == "routing"
    assert "Multiple handlers" in result.error
    assert calls == []


def test_dispatch_rejects_invalid_command():
    dispatcher = CommandDispatcher(HandlerRegistry())
    with pytest.raises(TypeError, match="command must be a Command"):
        dispatcher.dispatch("not a command")


def test_dispatch_result_rejects_success_with_error():
    from kernel.command.bus.command_dispatch_result import CommandDispatchResult

    with pytest.raises(ValueError, match="must not contain an error"):
        CommandDispatchResult(True, "cmd-42", "handler-1", error="no")
