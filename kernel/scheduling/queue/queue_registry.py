from kernel.core.registry.base_registry import BaseRegistry

from .scheduler_queue import SchedulerQueue


class QueueRegistry(
    BaseRegistry[SchedulerQueue],
):
    pass
