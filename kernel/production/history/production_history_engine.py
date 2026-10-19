from .production_history_entry import ProductionHistoryEntry


class ProductionHistoryEngine:

    def record(
        self,
        entry: ProductionHistoryEntry,
    ) -> ProductionHistoryEntry:
        return entry
