from __future__ import annotations

from .autonomous_runtime import (
    AutonomousRuntime,
)

from .agent_loop_state import (
    AgentLoopState,
)


class AgentLoop:

    def __init__(
        self,
        runtime: AutonomousRuntime,
    ) -> None:
        self._runtime = runtime

    def tick(self) -> None:
        if self._runtime.state != AgentLoopState.RUNNING:
            return
        self._runtime.next_cycle()
