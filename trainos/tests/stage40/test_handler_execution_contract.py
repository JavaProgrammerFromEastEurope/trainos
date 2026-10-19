import pytest

from kernel.command.command.command import Command
from kernel.command.command.command_priority import CommandPriority
from kernel.command.handler.command_handler import CommandHandler
from kernel.command.handler.handler_engine import HandlerEngine
from kernel.command.handler.handler_result import HandlerResult
from kernel.command.handler.handler_status import HandlerStatus


def make_command() -> Command:
    return Command("cmd-40", "inspect-sensor", CommandPriority.NORMAL)


def test_handler_invokes_executor_and_returns_its_output():
    calls = []

    def execute(command: Command) -> dict[str, str]:
        calls.append(command.command_id)
        return {"command": command.name, "state": "inspected"}

    handler = CommandHandler("sensor-handler", "sensor", executor=execute)
    result = HandlerEngine().execute(handler, make_command())

    assert result == HandlerResult(
        success=True,
        command_id="cmd-40",
        output={"command": "inspect-sensor", "state": "inspected"},
    )
    assert calls == ["cmd-40"]


def test_handler_without_executor_returns_explicit_failure():
    result = HandlerEngine().execute(CommandHandler("metadata", "metadata"), make_command())

    assert result.success is False
    assert result.output is None
    assert "no executor" in result.error


def test_handler_exception_becomes_diagnostic_failure():
    def broken_executor(command: Command) -> None:
        raise RuntimeError("sensor unavailable")

    result = HandlerEngine().execute(
        CommandHandler("broken", "broken", executor=broken_executor),
        make_command(),
    )

    assert result.success is False
    assert result.output is None
    assert result.error == "RuntimeError: sensor unavailable"


def test_handler_validates_executor_and_descriptor():
    with pytest.raises(ValueError):
        CommandHandler(" ", "name")
    with pytest.raises(ValueError):
        CommandHandler("id", " ")
    with pytest.raises(TypeError):
        CommandHandler("id", "name", status="idle")
    with pytest.raises(TypeError):
        CommandHandler("id", "name", executor="not-callable")
    with pytest.raises(TypeError):
        HandlerEngine().execute(object(), make_command())
    with pytest.raises(TypeError):
        HandlerEngine().execute(CommandHandler("id", "name"), object())
