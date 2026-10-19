from kernel.core.registry.base_registry import BaseRegistry

from .command_policy import CommandPolicy


class PolicyRegistry(BaseRegistry[CommandPolicy]):
    """Registry for CommandPolicy instances."""

    pass
