from kernel.core.registry.base_registry import BaseRegistry

from .persistence_snapshot import PersistenceSnapshot


class PersistenceSnapshotRegistry(
    BaseRegistry[PersistenceSnapshot],
):
    pass
