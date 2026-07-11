from kernel.core.registry.base_registry import BaseRegistry

from .treatment import Treatment


class TreatmentRegistry(
    BaseRegistry[Treatment],
):
    pass
