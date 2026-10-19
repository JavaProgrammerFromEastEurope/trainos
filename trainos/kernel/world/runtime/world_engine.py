from __future__ import annotations

from .world_runtime import (
    WorldRuntime,
)


class WorldEngine:

    def __init__(
        self,
    ) -> None:
        self._runtime = WorldRuntime()

    def tick(
        self,
    ) -> None:
        self._runtime.next_cycle()
