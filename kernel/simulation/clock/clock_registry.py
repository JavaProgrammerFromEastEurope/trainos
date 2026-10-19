from kernel.core.registry.base_registry import BaseRegistry

from .simulation_clock import SimulationClock


class ClockRegistry(
    BaseRegistry[SimulationClock],
):
    pass
