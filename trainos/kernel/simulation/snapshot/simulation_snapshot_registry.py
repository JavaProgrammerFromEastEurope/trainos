from kernel.core.registry.base_registry import BaseRegistry

from .simulation_snapshot import SimulationSnapshot


class SimulationSnapshotRegistry(
    BaseRegistry[SimulationSnapshot],
):
    pass
