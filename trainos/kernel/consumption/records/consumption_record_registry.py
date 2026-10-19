from kernel.core.registry.base_registry import BaseRegistry

from .consumption_record import ConsumptionRecord


class ConsumptionRecordRegistry(
    BaseRegistry[ConsumptionRecord],
):
    pass
