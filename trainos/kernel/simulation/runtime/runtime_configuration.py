from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class RuntimeConfiguration:

    auto_start: bool 			= False
    process_events: bool 	= True
    max_ticks: int = 0