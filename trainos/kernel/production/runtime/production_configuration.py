from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class ProductionConfiguration:

    auto_start: 				bool = True
    max_parallel_jobs: 	int = 4
    enable_scheduler: 	bool = True