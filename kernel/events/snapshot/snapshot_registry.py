from kernel.core.registry.base_registry import BaseRegistry

from .event_snapshot import EventSnapshot


class SnapshotRegistry(
    BaseRegistry[EventSnapshot],
):
    pass
