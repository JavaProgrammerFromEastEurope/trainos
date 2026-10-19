from kernel.core.registry.base_registry import BaseRegistry

from .workflow_execution import WorkflowExecution


class ExecutionRegistry(
    BaseRegistry[WorkflowExecution],
):
    pass
