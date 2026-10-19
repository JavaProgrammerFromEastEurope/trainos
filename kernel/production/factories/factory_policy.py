from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class FactoryPolicy:

    allow_parallel_jobs: 		bool
    require_active_status: 	bool