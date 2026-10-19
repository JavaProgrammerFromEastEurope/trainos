from kernel.core.registry.base_registry import BaseRegistry

from .consumption_history_entry import ConsumptionHistoryEntry


class ConsumptionHistoryRegistry(
    BaseRegistry[ConsumptionHistoryEntry],
):
    pass
