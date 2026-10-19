from kernel.core.registry.base_registry import BaseRegistry

from .simulation_history_entry import SimulationHistoryEntry


class SimulationHistoryRegistry(
    BaseRegistry[SimulationHistoryEntry],
):
    pass
