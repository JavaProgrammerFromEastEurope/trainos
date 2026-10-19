from __future__ import annotations

from .civil_right_set import CivilRightSet


class CivilRightRegistry:

    def __init__(self) -> None:
        self._rights: dict[str, CivilRightSet] = {}

    def register(self, right_set: CivilRightSet) -> None:
        self._rights[right_set.entity_id] = right_set

    def get(self, entity_id: str) -> CivilRightSet | None:
        return self._rights.get(entity_id)
