from dataclasses import dataclass

from .population_snapshot import PopulationSnapshot


@dataclass(frozen=True, slots=True)
class PopulationHistoryEntry:

    entry_id: 	str
    timestamp: 	str
    snapshot: PopulationSnapshot