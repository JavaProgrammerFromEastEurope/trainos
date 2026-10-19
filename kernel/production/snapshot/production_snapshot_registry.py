from kernel.core.registry.base_registry import BaseRegistry

from .production_snapshot import ProductionSnapshot


class ProductionSnapshotRegistry(
    BaseRegistry[ProductionSnapshot],
):
    pass
