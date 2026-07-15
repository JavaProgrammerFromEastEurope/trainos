from kernel.core.registry.base_registry import BaseRegistry

from .workflow_snapshot import WorkflowSnapshot


class SnapshotRegistry(
    BaseRegistry[WorkflowSnapshot],
):
    pass
