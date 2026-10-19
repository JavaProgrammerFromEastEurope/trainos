from __future__ import annotations

from .intelligence_cycle import IntelligenceCycle


class IntelligenceRuntimeRegistry:

    def __init__(self) -> None:
        self._cycles: list[IntelligenceCycle] = []

    def register(self, cycle: IntelligenceCycle) -> None:
        self._cycles.append(cycle)

    def cycles(self) -> tuple[IntelligenceCycle, ...]:
        return tuple(self._cycles)
