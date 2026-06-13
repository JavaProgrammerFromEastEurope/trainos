from __future__ import annotations

from .agent_registry import (
    AgentRegistry,
)

from .agent import Agent


class AgentManager:

    def __init__(self) -> None:
        self._registry = AgentRegistry()

    def add(
        self,
        agent: Agent,
    ) -> None:
        self._registry.register(
            agent,
        )

    def get(
        self,
        agent_id: str,
    ) -> Agent | None:
        return self._registry.get(
            agent_id,
        )

    def agents(
        self,
    ) -> list[Agent]:
        return self._registry.all()
