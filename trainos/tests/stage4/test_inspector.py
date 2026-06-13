from trainos.kernel.command_bus.command_history import CommandHistory
from trainos.kernel.command_bus.command_record import CommandRecord
from trainos.kernel.command_bus.debug.command_inspector import CommandInspector


def test_inspector():

    history = CommandHistory()
    history.append(CommandRecord("cmd", {"a": 1}))
    inspector = CommandInspector(history)
    result = inspector.inspect()

    assert len(result) == 1
    assert result[0].command_name == "cmd"
