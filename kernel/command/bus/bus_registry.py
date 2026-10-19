from kernel.core.registry.base_registry import BaseRegistry

from .command_bus import CommandBus


class BusRegistry(BaseRegistry[CommandBus]):
    """Registry for CommandBus instances."""

    pass
