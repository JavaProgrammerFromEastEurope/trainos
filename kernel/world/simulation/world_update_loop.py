from __future__ import annotations

from .simulation_context import (
    SimulationContext,
)


class WorldUpdateLoop:

    def update(
        self,
        context: SimulationContext,
        dt: float,
    ) -> None:
        context.tick.value += 1
        context.clock.time += dt
