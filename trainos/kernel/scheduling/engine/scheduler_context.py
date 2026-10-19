from dataclasses import dataclass

from kernel.scheduling.queue.scheduler_queue import SchedulerQueue


@dataclass(slots=True)
class SchedulerContext:

    queue: SchedulerQueue
