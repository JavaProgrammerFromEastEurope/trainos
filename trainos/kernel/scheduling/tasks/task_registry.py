from kernel.core.registry.base_registry import BaseRegistry

from .scheduler_task import SchedulerTask


class TaskRegistry(
    BaseRegistry[SchedulerTask],
):
    pass
