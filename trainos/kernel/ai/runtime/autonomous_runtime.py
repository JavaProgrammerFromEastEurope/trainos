from __future__ import annotations

from .agent_loop_state import (
    AgentLoopState,
)

from .autonomous_cycle import (
    AutonomousCycle,
)


class AutonomousRuntime:

    def __init__(self) -> None:
        self._state = AgentLoopState.STOPPED
        self._cycle = 0

    def start(self) -> None:
        self._state = AgentLoopState.RUNNING

    def stop(self) -> None:
        self._state = AgentLoopState.STOPPED

    def pause(self) -> None:
        self._state = AgentLoopState.PAUSED

    def next_cycle(
        self,
    ) -> AutonomousCycle:
        self._cycle += 1
        return AutonomousCycle(
            cycle_id=self._cycle,
        )

    @property
    def state(
        self,
    ) -> AgentLoopState:
        return self._state
