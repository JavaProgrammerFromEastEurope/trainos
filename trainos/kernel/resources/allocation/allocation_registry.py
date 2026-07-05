from kernel.core.registry.base_registry import BaseRegistry

from .resource_allocation import ResourceAllocation


class AllocationRegistry(
    BaseRegistry[ResourceAllocation],
):
    pass
