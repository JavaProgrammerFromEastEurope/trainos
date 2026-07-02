from __future__ import annotations

from .constitutional_evolution import ConstitutionalEvolution


class EvolutionRegistry:

    def __init__(self) -> None:
        self._entries: list[ConstitutionalEvolution] = []

    def register(
        self,
        evolution: ConstitutionalEvolution,
    ) -> None:
        self._entries.append(evolution)

    def entries(
        self,
    ) -> tuple[ConstitutionalEvolution, ...]:
        return tuple(self._entries)
