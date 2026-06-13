from __future__ import annotations

from .command import Command
from .command_service import CommandService
from .command_context import CommandContext
from .command_result import CommandResult


class CommandBus:

    def __init__(self, service: CommandService) -> None:
        self._service = service

    def send(
        self,
        command: Command,
        context: CommandContext | None = None,
    ) -> CommandResult:

        if context is None:
            context = CommandContext()

        raw = self._service.execute(command, context)

        # 🔥 NORMALIZATION LAYER
        if isinstance(raw, CommandResult):
            return raw

        return CommandResult(
            success=True,
            data=raw,
        )
