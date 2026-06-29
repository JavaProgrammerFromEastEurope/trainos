from __future__ import annotations

from .civilization_intent import CivilizationIntent


class IntentRegistry:

    def __init__(self) -> None:
        self._intents: list[CivilizationIntent] = []

    def register(self, intent: CivilizationIntent) -> None:
        self._intents.append(intent)

    def intents(self) -> tuple[CivilizationIntent, ...]:
        return tuple(self._intents)
