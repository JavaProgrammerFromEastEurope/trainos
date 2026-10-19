from kernel.core.registry.base_registry import BaseRegistry

from .factory import Factory


class FactoryRegistry(
    BaseRegistry[Factory]
):
    pass