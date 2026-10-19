from dataclasses import FrozenInstanceError
import pytest

from kernel.command.command.command import Command
from kernel.command.command.command_engine import CommandEngine
from kernel.command.command.command_priority import CommandPriority
from kernel.command.command.command_status import CommandStatus


def test_command_is_validated_immutable_and_transitions_through_engine():
    command = Command("cmd-1", "rebuild-index", CommandPriority.HIGH)
    assert command.status is CommandStatus.CREATED
    with pytest.raises(FrozenInstanceError):
        command.name = "mutated"
    accepted = CommandEngine().accept(command)
    executed = CommandEngine().execute(accepted)
    assert accepted.status is CommandStatus.ACCEPTED
    assert executed.status is CommandStatus.EXECUTED
    assert (executed.command_id, executed.name, executed.priority) == (
        command.command_id,
        command.name,
        command.priority,
    )
    for args in [
        ("", "name", CommandPriority.NORMAL),
        ("id", "", CommandPriority.NORMAL),
    ]:
        with pytest.raises(ValueError):
            Command(*args)
    with pytest.raises(TypeError):
        Command("id", "name", "high")
