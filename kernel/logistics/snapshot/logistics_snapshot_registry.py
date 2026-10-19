from kernel.core.registry.base_registry import BaseRegistry

from .logistics_snapshot import LogisticsSnapshot


class LogisticsSnapshotRegistry(
    BaseRegistry[LogisticsSnapshot],
):
    pass