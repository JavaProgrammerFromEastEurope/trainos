from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class PopulationConfiguration:

    auto_start: 					bool = True
    enable_scheduler: 		bool = True
    max_updates_per_cycle: int = 1000