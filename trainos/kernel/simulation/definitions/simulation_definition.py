from dataclasses import dataclass

from .simulation_category import SimulationCategory
from .simulation_type import SimulationType


@dataclass(frozen=True, slots=True)
class SimulationDefinition:

    simulation_id: 	str
    name: 					str
    simulation_type: SimulationType
    category: SimulationCategory