from dataclasses import dataclass

from kernel.simulation.scheduler.scheduler_status import SchedulerStatus


@dataclass(frozen=True, slots=True)
class SchedulerSnapshot:

    scheduler_id: str
    status: SchedulerStatus
