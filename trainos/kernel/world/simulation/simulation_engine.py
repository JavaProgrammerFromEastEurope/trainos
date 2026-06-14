from __future__ import annotations

from .simulation_runtime import (
    SimulationRuntime,
)

from .simulation_context import (
    SimulationContext,
)

from .world_update_loop import (
    WorldUpdateLoop,
)


class SimulationEngine:

    def __init__(
        self,
    ) -> None:
        self._runtime = SimulationRuntime()
        self._loop 		= WorldUpdateLoop()

    def tick(
        self,
        dt: float,
    ) -> None:
        context = SimulationContext(
            tick=self._runtime.tick,
            clock=self._runtime.clock,
        )
        self._loop.update(
            context,
            dt,
        )
