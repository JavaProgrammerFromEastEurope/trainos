from dataclasses import dataclass

from kernel.population.professions.profession_type import ProfessionType


@dataclass(frozen=True, slots=True)
class ProfessionSnapshot:

    profession_id: str
    profession_type: ProfessionType