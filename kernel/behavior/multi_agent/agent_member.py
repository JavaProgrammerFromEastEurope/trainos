from dataclasses import dataclass

from .agent_role import (
    AgentRole,
)


@dataclass
class AgentMember:

    id: str
    role: AgentRole
