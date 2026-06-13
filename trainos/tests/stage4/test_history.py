from trainos.kernel.command_bus.command_history import CommandHistory
from trainos.kernel.command_bus.command_record import CommandRecord


def test_history():

    history = CommandHistory()
    history.append(CommandRecord("cmd", {"a": 1}))
    
    assert len(history.all()) == 1
    assert history.last().command_name == "cmd"