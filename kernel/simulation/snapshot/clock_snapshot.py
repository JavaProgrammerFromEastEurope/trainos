from dataclasses import dataclass

from kernel.simulation.clock.clock_status import ClockStatus


@dataclass(frozen=True, slots=True)
class ClockSnapshot:

    clock_id: str
    tick: int
    status: ClockStatus
