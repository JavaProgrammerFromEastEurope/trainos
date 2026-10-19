from __future__ import annotations

from .cognitive_cycle import (
    CognitiveCycle,
)


class CognitiveLoop:

    def __init__(
        self,
    ) -> None:
        self._cycle = 0

    def next_cycle(
        self,
    ) -> CognitiveCycle:
        self._cycle += 1
        return CognitiveCycle(cycle_id=self._cycle)
