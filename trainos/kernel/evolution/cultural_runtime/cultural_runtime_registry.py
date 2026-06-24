from __future__ import annotations

from .cultural_tick import CulturalTick


class CulturalRuntimeRegistry:

    def __init__(self) -> None:
        self._ticks: list[CulturalTick] = []

    def register(self, tick: CulturalTick) -> None:
        self._ticks.append(tick)

    def ticks(self) -> tuple[CulturalTick, ...]:
        return tuple(self._ticks)
