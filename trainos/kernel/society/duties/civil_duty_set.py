from dataclasses import dataclass

from .civil_duty import CivilDuty


@dataclass(frozen=True)
class CivilDutySet:

    entity_id: str
    duties: tuple[CivilDuty, ...]