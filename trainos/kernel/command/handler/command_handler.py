from dataclasses import dataclass, field
from typing import Any, Callable

from ..command.command import Command
from .handler_status import HandlerStatus


CommandExecutor = Callable[[Command], Any]


@dataclass(frozen=True, slots=True)
class CommandHandler:
    """Immutable handler descriptor with an optional executable callback.

    A handler without an executor is a registration/metadata object only; it
    must not be reported as having executed a command successfully.
    """

    handler_id: str
    name: str
    status: HandlerStatus = HandlerStatus.IDLE
    executor: CommandExecutor | None = field(default=None, repr=False, compare=False)

    def __post_init__(self) -> None:
        if not isinstance(self.handler_id, str) or not self.handler_id.strip():
            raise ValueError("handler_id must not be empty")
        if not isinstance(self.name, str) or not self.name.strip():
            raise ValueError("name must not be empty")
        if not isinstance(self.status, HandlerStatus):
            raise TypeError("status must be a HandlerStatus")
        if self.executor is not None and not callable(self.executor):
            raise TypeError("executor must be callable or None")
