from dataclasses import dataclass

from .principle_type import PrincipleType


@dataclass(frozen=True)
class CivilizationPrinciple:

    name: str
    description: str
    type: PrincipleType