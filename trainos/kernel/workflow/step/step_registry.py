from kernel.core.registry.base_registry import BaseRegistry

from .workflow_step import WorkflowStep


class StepRegistry(
    BaseRegistry[WorkflowStep],
):
    pass
