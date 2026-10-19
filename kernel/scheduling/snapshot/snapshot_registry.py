from kernel.core.registry.base_registry import BaseRegistry

from .scheduler_snapshot import SchedulerSnapshot


class SnapshotRegistry(
    BaseRegistry[SchedulerSnapshot],
):
    pass
