from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class ConsumptionConfiguration:

    auto_start: 			bool = True
    max_parallel_jobs: int = 16
    enable_scheduler: bool = True