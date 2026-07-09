from kernel.core.registry.base_registry import BaseRegistry

from .consumption_job import ConsumptionJob


class ConsumptionJobRegistry(
    BaseRegistry[ConsumptionJob],
):
    pass
