from .simulation_history_entry import SimulationHistoryEntry


class SimulationHistoryEngine:

    def record(
        self,
        entry: SimulationHistoryEntry,
    ) -> SimulationHistoryEntry:
        return entry
