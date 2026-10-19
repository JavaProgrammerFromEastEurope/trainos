from dataclasses import dataclass

from .simulation_history_snapshot import SimulationHistorySnapshot


@dataclass(frozen=True, slots=True)
class SimulationHistoryEntry:

    entry_id: 	str
    timestamp: 	str
    snapshot: SimulationHistorySnapshot
