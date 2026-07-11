from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class SecurityConfiguration:

    auto_dispatch: bool 				= True
    enable_scheduler: bool 			= True
    max_incidents_per_cycle: int = 1000