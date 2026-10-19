from dataclasses import dataclass

from .profession_category import ProfessionCategory
from .profession_type import ProfessionType


@dataclass(frozen=True, slots=True)
class Profession:

    profession_id: 	str
    name: 					str
    profession_type: ProfessionType
    category: ProfessionCategory