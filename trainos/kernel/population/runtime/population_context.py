from dataclasses import dataclass

from .population_configuration import PopulationConfiguration


@dataclass(slots=True)
class PopulationContext:

    configuration: PopulationConfiguration
