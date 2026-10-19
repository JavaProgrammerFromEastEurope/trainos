from kernel.core.registry.base_registry import BaseRegistry

from .execution_context import ExecutionContext


class ContextRegistry(
    BaseRegistry[ExecutionContext],
):
    pass
