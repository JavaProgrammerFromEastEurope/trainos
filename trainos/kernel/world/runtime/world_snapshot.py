from dataclasses import dataclass


@dataclass
class WorldSnapshot:
    entity_count: int
    simulation_time: float
