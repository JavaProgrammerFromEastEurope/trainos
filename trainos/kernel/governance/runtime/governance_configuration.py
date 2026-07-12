from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class GovernanceConfiguration:

    auto_execute_decisions: bool = True
    enable_scheduler: 			bool = True
    max_decisions_per_cycle: int = 1000