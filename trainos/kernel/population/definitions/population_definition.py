from dataclasses import dataclass

from .population_category import PopulationCategory
from .population_type import PopulationType


@dataclass(frozen=True, slots=True)
class PopulationDefinition:

    population_id: 	str
    name: 					str
    population_type: PopulationType
    category: PopulationCategory