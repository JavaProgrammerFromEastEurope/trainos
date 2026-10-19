from __future__ import annotations

from .civilization_principle import CivilizationPrinciple


class PrincipleRegistry:

    def __init__(self) -> None:
        self._principles: list[CivilizationPrinciple] = []

    def register(self, principle: CivilizationPrinciple) -> None:
        self._principles.append(principle)

    def principles(self) -> tuple[CivilizationPrinciple, ...]:
        return tuple(self._principles)
