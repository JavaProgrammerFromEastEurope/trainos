from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class ProductionJobPolicy:

    allow_parallel_jobs: bool = True
    auto_start: bool = False