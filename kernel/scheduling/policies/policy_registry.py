from kernel.core.registry.base_registry import BaseRegistry

from .scheduler_policy import SchedulerPolicy


class PolicyRegistry(
    BaseRegistry[SchedulerPolicy],
):
    pass
