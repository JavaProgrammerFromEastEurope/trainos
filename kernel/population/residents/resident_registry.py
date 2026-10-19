from kernel.core.registry.base_registry import BaseRegistry

from .resident import Resident


class ResidentRegistry(
    BaseRegistry[Resident],
):
    pass
