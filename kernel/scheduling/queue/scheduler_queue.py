from dataclasses import dataclass, field

from kernel.scheduling.tasks.scheduler_task import SchedulerTask
from .queue_status import QueueStatus
from .queue_policy import QueuePolicy


@dataclass(slots=True)
class SchedulerQueue:

    tasks: list[SchedulerTask] = field(default_factory=list)

    status: QueueStatus = QueueStatus.EMPTY
    policy: QueuePolicy = QueuePolicy.PRIORITY
