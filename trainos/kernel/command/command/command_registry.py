from kernel.core.registry.base_registry import BaseRegistry

from .command import Command


class CommandRegistry(BaseRegistry[Command]):
    """Registry for Command instances."""

    pass
