from kernel.core.registry.base_registry import BaseRegistry

from .production_job import ProductionJob


class ProductionJobRegistry(
    BaseRegistry[ProductionJob],
):
    pass
