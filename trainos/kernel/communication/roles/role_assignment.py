from __future__ import annotations

from dataclasses import dataclass

from .agent_role import AgentRole


@dataclass
class RoleAssignment:

    agent_id: str

    role: AgentRole
