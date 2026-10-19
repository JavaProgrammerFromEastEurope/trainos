from __future__ import annotations

from .agent import Agent
from .agent_state import AgentState


class AgentExecutor:

    def execute(
        self,
        agent: Agent,
    ) -> None:
        agent.state = AgentState.THINKING
        agent.state = AgentState.EXECUTING
        agent.state = AgentState.IDLE
