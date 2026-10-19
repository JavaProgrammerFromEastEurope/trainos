from kernel.core.registry.base_registry import BaseRegistry

from .decision import Decision


class DecisionRegistry(
    BaseRegistry[Decision],
):
    pass
