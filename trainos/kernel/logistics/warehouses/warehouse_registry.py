from kernel.core.registry.base_registry import BaseRegistry

from .warehouse import Warehouse


class WarehouseRegistry(
    BaseRegistry[Warehouse],
):
    pass
