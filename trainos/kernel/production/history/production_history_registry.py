from ...core.registry.base_registry import BaseRegistry

from .production_history_entry import ProductionHistoryEntry


class ProductionHistoryRegistry(
    BaseRegistry[ProductionHistoryEntry],
):
    pass
