from __future__ import annotations

from .world_cycle import (
    WorldCycle,
)


class WorldLoop:

    def __init__(
        self,
    ) -> None:
        self._cycle = 0

    def next_cycle(
        self,
    ) -> WorldCycle:
        self._cycle += 1
        return WorldCycle(
            cycle_id=self._cycle,
        )
