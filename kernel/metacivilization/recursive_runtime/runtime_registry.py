from __future__ import annotations

from .runtime_tick import RuntimeTick


class RuntimeRegistry:

    def __init__(self) -> None:
        self._ticks: list[RuntimeTick] = []

    def register(self, tick: RuntimeTick) -> None:
        self._ticks.append(tick)

    def ticks(self) -> tuple[RuntimeTick, ...]:
        return tuple(self._ticks)
