from kernel.core.registry.base_registry import BaseRegistry

from .workflow import Workflow


class WorkflowRegistry(
    BaseRegistry[Workflow],
):
    pass
