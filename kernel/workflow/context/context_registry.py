from kernel.core.registry.base_registry import BaseRegistry

from .workflow_context import WorkflowContext


class ContextRegistry(
    BaseRegistry[WorkflowContext],
):
    pass
