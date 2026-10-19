from dataclasses import dataclass

from .clock_status import ClockStatus


@dataclass(frozen=True, slots=True)
class SimulationClock:

    clock_id: str
    tick: 		int
    status: ClockStatus