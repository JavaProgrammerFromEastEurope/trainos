from __future__ import annotations

from .institution import (
    Institution,
)


class InstitutionRegistry:

    def __init__(self) -> None:
        self._institutions: list[Institution] = []

    def add(self, institution: Institution) -> None:
        self._institutions.append(institution)

    def institutions(self) -> tuple[Institution, ...]:
        return tuple(self._institutions)
