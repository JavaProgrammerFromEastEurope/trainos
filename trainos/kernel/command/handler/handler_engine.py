from __future__ import annotations

from ..command.command import Command
from .command_handler import CommandHandler
from .handler_result import HandlerResult


class HandlerEngine:
    """Executes a command through a handler.

    The current stage provides a deterministic successful execution scaffold.
    Actual handler dispatch can be added without changing the result contract.
    """

    def execute(
        self,
        handler: CommandHandler,
        command: Command,
    ) -> HandlerResult:
        if not handler.handler_id:
            raise ValueError("handler.handler_id must not be empty")
        if not command.command_id:
            raise ValueError("command.command_id must not be empty")
        return HandlerResult(success=True, command_id=command.command_id)
