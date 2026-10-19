from __future__ import annotations

from .civil_duty_set import CivilDutySet


class CivilDutyRegistry:

    def __init__(self) -> None:
        self._duties: dict[str, CivilDutySet] = {}

    def register(self, duty_set: CivilDutySet) -> None:
        self._duties[duty_set.entity_id] = duty_set

    def get(self, entity_id: str) -> CivilDutySet | None:
        return self._duties.get(entity_id)
