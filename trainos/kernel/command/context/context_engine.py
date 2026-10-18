from .command_context import CommandContext
from .context_state import ContextState


class ContextEngine:

    def activate(
        self,
        context: CommandContext,
    ) -> CommandContext:
        return CommandContext(
            command_id=context.command_id,
            metadata=context.metadata,
            state=ContextState.ACTIVE,
        )


    def close(
        self,
        context: CommandContext,
    ) -> CommandContext:
        return CommandContext(
            command_id=context.command_id,
            metadata=context.metadata,
            state=ContextState.CLOSED,
        )
