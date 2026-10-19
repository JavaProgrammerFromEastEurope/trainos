from kernel.core.registry.base_registry import BaseRegistry

from .command_execution import CommandExecution


class ExecutionRegistry(BaseRegistry[CommandExecution]):
    """Registry for CommandExecution instances."""

    pass
