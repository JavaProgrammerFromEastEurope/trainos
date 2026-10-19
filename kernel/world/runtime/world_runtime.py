from __future__ import annotations

from .world_cycle import WorldCycle
from .world_state import WorldState
from .world_loop import WorldLoop


class WorldRuntime:

    def __init__(
        self,
    ) -> None:
        self._state = WorldState.STOPPED
        self._loop 	= WorldLoop()

    def start(
        self,
    ) -> None:
        self._state = WorldState.RUNNING

    def stop(
        self,
    ) -> None:
        self._state = WorldState.STOPPED

    def pause(
        self,
    ) -> None:
        self._state = WorldState.PAUSED

    def next_cycle(
        self,
    ) -> WorldCycle:
        return self._loop.next_cycle()

    @property
    def state(
        self,
    ) -> WorldState:
        return self._state
