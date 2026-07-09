from .population_history_entry import PopulationHistoryEntry


class PopulationHistoryEngine:

    def record(
        self,
        entry: PopulationHistoryEntry,
    ) -> PopulationHistoryEntry:
        return entry
