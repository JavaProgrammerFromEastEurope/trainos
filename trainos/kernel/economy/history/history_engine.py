from .economic_history_entry import EconomicHistoryEntry


class HistoryEngine:

    def record(
        self,
        entry: EconomicHistoryEntry,
    ) -> EconomicHistoryEntry:
        return entry
