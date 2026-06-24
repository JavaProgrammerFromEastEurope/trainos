from __future__ import annotations

from .narrative import Narrative


class NarrativeRegistry:

    def __init__(self) -> None:
        self._narratives: list[Narrative] = []

    def register(self, narrative: Narrative) -> None:
        self._narratives.append(narrative)

    def narratives(self) -> tuple[Narrative, ...]:
        return tuple(self._narratives)
