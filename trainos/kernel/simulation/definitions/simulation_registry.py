from kernel.core.registry.base_registry import BaseRegistry

from .simulation_definition import SimulationDefinition


class SimulationRegistry(
    BaseRegistry[SimulationDefinition],
):
    pass
