from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class SimulationHistorySnapshot:

    snapshot_id: 	str
    tick: 				int
    population: 	int