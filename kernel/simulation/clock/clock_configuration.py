from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class ClockConfiguration:

    tick_duration: 	int = 1
    max_ticks: 			int = 0