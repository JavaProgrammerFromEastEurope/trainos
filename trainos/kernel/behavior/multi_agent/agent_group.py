from __future__ import annotations

from .agent_member import (
    AgentMember,
)


class AgentGroup:

    def __init__(
        self,
    ) -> None:
        self._members: list[AgentMember] = []

    def add(self, member: AgentMember) -> None:
        self._members.append(member)

    def members(
        self,
    ) -> tuple[AgentMember, ...]:
        return tuple(self._members)
