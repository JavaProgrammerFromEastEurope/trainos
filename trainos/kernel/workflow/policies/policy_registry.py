from kernel.core.registry.base_registry import BaseRegistry

from .workflow_policy import WorkflowPolicy


class PolicyRegistry(
    BaseRegistry[WorkflowPolicy],
):
    pass
