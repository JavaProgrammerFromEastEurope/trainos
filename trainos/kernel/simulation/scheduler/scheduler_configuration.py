from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class SchedulerConfiguration:

    max_events_per_tick: int 	= 100
    auto_process: bool 				= True