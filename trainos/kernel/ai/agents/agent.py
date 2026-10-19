from __future__ import annotations

from dataclasses import dataclass, field

from .agent_state 	import AgentState
from .agent_context import AgentContext


@dataclass
class Agent:

    id: str
    name: str
    context: AgentContext
    state: AgentState = AgentState.IDLE