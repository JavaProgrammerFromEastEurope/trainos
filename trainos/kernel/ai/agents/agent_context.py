from __future__ import annotations

from dataclasses import dataclass

from kernel.ai.memory.memory_manager import (
    MemoryManager,
)

from kernel.ai.goals.goal_manager import (
    GoalManager,
)


@dataclass
class AgentContext:
    memory: MemoryManager
    goals: GoalManager
