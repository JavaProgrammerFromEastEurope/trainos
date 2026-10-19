from kernel.core.registry.base_registry import BaseRegistry

from .population_snapshot import PopulationSnapshot


class PopulationSnapshotRegistry(
    BaseRegistry[PopulationSnapshot],
):
    pass