from kernel.core.registry.base_registry import BaseRegistry

from .execution_result import ExecutionResult


class SchedulerRegistry(
    BaseRegistry[ExecutionResult],
):
    pass
