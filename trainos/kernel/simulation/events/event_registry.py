from kernel.core.registry.base_registry import BaseRegistry

from .simulation_event import SimulationEvent


class EventRegistry(
    BaseRegistry[SimulationEvent],
):
    pass
