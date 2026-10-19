from __future__ import annotations

from .cognitive_cycle import CognitiveCycle


class CognitiveHistory:

    def __init__(
        self,
    ) -> None:
        self._history: list[CognitiveCycle] = []

    def add(
        self,
        cycle: CognitiveCycle,
    ) -> None:
        self._history.append(cycle)

    def records(
        self,
    ) -> tuple[CognitiveCycle, ...]:
        return tuple(self._history)
