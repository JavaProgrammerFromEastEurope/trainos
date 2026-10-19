from __future__ import annotations

from .agent_node import AgentNode


class AgentNetwork:

    def __init__(self) -> None:
        self._agents: list[AgentNode] = []

    def add(self, agent: AgentNode) -> None:
        self._agents.append(agent)

    def agents(self) -> tuple[AgentNode, ...]:
        return tuple(self._agents)
