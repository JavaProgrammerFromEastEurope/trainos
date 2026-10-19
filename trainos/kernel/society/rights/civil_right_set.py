from dataclasses import dataclass

from .civil_right import CivilRight


@dataclass(frozen=True)
class CivilRightSet:

    entity_id: str
    rights: tuple[CivilRight, ...]