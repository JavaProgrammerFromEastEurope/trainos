from kernel.core.registry.base_registry import BaseRegistry

from .command_context import CommandContext


class ContextRegistry(BaseRegistry[CommandContext]):
    """Registry for CommandContext instances."""

    pass
