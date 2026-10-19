from __future__ import annotations

from ..command.command import Command
from .command_handler import CommandHandler
from .handler_result import HandlerResult


class HandlerEngine:
    """Invoke a handler and report actual execution rather than assumed success."""

    def execute(
        self,
        handler: CommandHandler,
        command: Command,
    ) -> HandlerResult:
        if not isinstance(handler, CommandHandler):
            raise TypeError("handler must be a CommandHandler")
        if not isinstance(command, Command):
            raise TypeError("command must be a Command")
        if not handler.handler_id.strip():
            raise ValueError("handler.handler_id must not be empty")
        if not command.command_id.strip():
            raise ValueError("command.command_id must not be empty")

        if handler.executor is None:
            return HandlerResult(
                success=False,
                command_id=command.command_id,
                error=f"Handler '{handler.handler_id}' has no executor",
            )

        try:
            output = handler.executor(command)
        except Exception as exc:
            # Convert ordinary handler failures into an explicit result so the
            # caller can make a policy decision; do not disguise them as success.
            detail = str(exc).strip()
            error = f"{type(exc).__name__}: {detail}" if detail else type(exc).__name__
            return HandlerResult(
                success=False,
                command_id=command.command_id,
                error=error,
            )

        return HandlerResult(
            success=True,
            command_id=command.command_id,
            output=output,
        )
