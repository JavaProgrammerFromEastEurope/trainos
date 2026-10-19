from kernel.core.registry.base_registry import BaseRegistry

from .population_definition import PopulationDefinition


class PopulationRegistry(
    BaseRegistry[PopulationDefinition]
):
    pass