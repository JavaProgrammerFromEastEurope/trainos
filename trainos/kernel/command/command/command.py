from dataclasses import dataclass

from .command_priority import CommandPriority
from .command_status import CommandStatus


@dataclass(frozen=True, slots=True)
class Command:
    """Immutable command descriptor."""

    command_id: str
    name: str
    priority: CommandPriority
    status: CommandStatus = CommandStatus.CREATED

    def __post_init__(self) -> None:
        if not self.command_id.strip():
            raise ValueError("command_id must not be empty")
        if not self.name.strip():
            raise ValueError("name must not be empty")
        if not isinstance(self.priority, CommandPriority):
            raise TypeError("priority must be a CommandPriority")
        if not isinstance(self.status, CommandStatus):
            raise TypeError("status must be a CommandStatus")
