from kernel.core.registry.base_registry import BaseRegistry

from .command_handler import CommandHandler


class HandlerRegistry(BaseRegistry[CommandHandler]):
    """Registry for CommandHandler instances."""

    pass
