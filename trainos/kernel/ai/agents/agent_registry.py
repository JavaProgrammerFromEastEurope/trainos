from __future__ import annotations

from typing import Dict
from .agent import Agent


class AgentRegistry:

    def __init__(self) -> None:
        self._agents: Dict[
            str,
            Agent,
        ] = {}

    def register(
        self,
        agent: Agent,
    ) -> None:
        self._agents[agent.id] = agent

    def get(
        self,
        agent_id: str,
    ) -> Agent | None:
        return self._agents.get(
            agent_id,
        )

    def all(
        self,
    ) -> list[Agent]:
        return list(self._agents.values())
