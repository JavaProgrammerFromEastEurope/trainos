from __future__ import annotations

from typing import Type

from .command import Command
from .command_handler import CommandHandler
from .command_context import CommandContext
from .command_result 	import CommandResult


class CommandService:

    def __init__(self) -> None:
        self._handlers: dict[
            Type[Command],
            CommandHandler,
        ] = {}

    def register(
        self,
        command_type: Type[Command],
        handler: CommandHandler,
    ) -> None:
        self._handlers[command_type] = handler

    def execute(
        self,
        command: Command,
        context: CommandContext | None = None,
    ) -> CommandResult:
        if context is None:
            context = CommandContext()
        handler = self._handlers.get(
            type(command),
        )
        if handler is None:
            return CommandResult(
                success=False,
                error="Handler not found",
            )
        return handler.execute(
            command,
            context,
        )
