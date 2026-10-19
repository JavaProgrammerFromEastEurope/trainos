from kernel.core.registry.base_registry import BaseRegistry

from .consumption_snapshot import ConsumptionSnapshot


class ConsumptionSnapshotRegistry(
    BaseRegistry[ConsumptionSnapshot],
):
    pass
