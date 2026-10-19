from kernel.core.registry.base_registry import BaseRegistry

from .production_output import ProductionOutput


class ProductionOutputRegistry(
    BaseRegistry[ProductionOutput],
):
    pass
