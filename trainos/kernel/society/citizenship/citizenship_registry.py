from __future__ import annotations

from .citizenship import Citizenship


class CitizenshipRegistry:

    def __init__(self) -> None:
        self._citizenship: dict[str, Citizenship] = {}

    def register(self, citizenship: Citizenship) -> None:
        self._citizenship[citizenship.entity_id] = citizenship

    def get(self, entity_id: str) -> Citizenship | None:
        return self._citizenship.get(entity_id)
