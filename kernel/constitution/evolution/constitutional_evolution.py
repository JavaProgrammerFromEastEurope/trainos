from dataclasses import dataclass

from .evolution_type import EvolutionType


@dataclass(frozen=True)
class ConstitutionalEvolution:

    article: 			str
    evolution: EvolutionType
    description: 	str