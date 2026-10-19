from __future__ import annotations

from .simulation_state import (
    SimulationState,
)

from .simulation_tick import (
    SimulationTick,
)

from .simulation_clock import (
    SimulationClock,
)


class SimulationRuntime:

    def __init__(
        self,
    ) -> None:

        self._state = SimulationState.STOPPED
        self._tick = SimulationTick(
            0,
        )
        self._clock = SimulationClock()

    def start(
        self,
    ) -> None:
        self._state = SimulationState.RUNNING

    def stop(
        self,
    ) -> None:
        self._state = SimulationState.STOPPED

    def pause(
        self,
    ) -> None:
        self._state = SimulationState.PAUSED

    @property
    def state(
        self,
    ) -> SimulationState:
        return self._state

    @property
    def tick(
        self,
    ) -> SimulationTick:
        return self._tick

    @property
    def clock(
        self,
    ) -> SimulationClock:
        return self._clock
