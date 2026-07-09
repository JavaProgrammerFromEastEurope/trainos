from .consumption_history_entry import ConsumptionHistoryEntry


class ConsumptionHistoryEngine:

    def record(
        self,
        entry: ConsumptionHistoryEntry,
    ) -> ConsumptionHistoryEntry:
        return entry