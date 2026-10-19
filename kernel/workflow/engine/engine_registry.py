from kernel.core.registry.base_registry import BaseRegistry

from .workflow_engine import WorkflowEngine


class EngineRegistry(
    BaseRegistry[WorkflowEngine],
):
    pass
