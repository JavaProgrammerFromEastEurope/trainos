from kernel.core.registry.base_registry import BaseRegistry

from .resource_consumption import ResourceConsumption


class ConsumptionRegistry(
    BaseRegistry[ResourceConsumption],
):
    pass
