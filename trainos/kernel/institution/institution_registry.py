from __future__ import annotations

from .institution import Institution


class InstitutionRegistry:

    def __init__(self) -> None:
        self._institutions: dict[str, Institution] = {}

    def register(self, institution: Institution) -> None:
        self._institutions[institution.institution_id] = institution

    def get(self, institution_id: str) -> Institution | None:
        return self._institutions.get(institution_id)

    def exists(self, institution_id: str) -> bool:
        return institution_id in self._institutions

    def institutions(self) -> tuple[Institution, ...]:
        return tuple(self._institutions.values())
