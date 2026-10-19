from dataclasses import dataclass

from .queue_snapshot import QueueSnapshot
from .timer_snapshot import TimerSnapshot
from .execution_snapshot import ExecutionSnapshot


@dataclass(frozen=True, slots=True)
class SchedulerSnapshot:

    snapshot_id: str
    queue: 			QueueSnapshot
    timer: 			TimerSnapshot
    execution: 	ExecutionSnapshot