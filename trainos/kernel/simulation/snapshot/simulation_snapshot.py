from dataclasses import dataclass


from .clock_snapshot import ClockSnapshot
from .event_snapshot import EventSnapshot
from .runtime_snapshot import RuntimeSnapshot
from .scheduler_snapshot import SchedulerSnapshot


@dataclass(frozen=True, slots=True)
class SimulationSnapshot:

    snapshot_id: 	str
    clock: 				ClockSnapshot
    runtime: 			RuntimeSnapshot
    scheduler: 		SchedulerSnapshot
    events: 			tuple[EventSnapshot, ...]