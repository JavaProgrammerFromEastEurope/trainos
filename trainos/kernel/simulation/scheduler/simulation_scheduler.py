from dataclasses import dataclass

from .scheduler_status import SchedulerStatus


@dataclass(frozen=True, slots=True)
class SimulationScheduler:

    scheduler_id: str
    status: SchedulerStatus