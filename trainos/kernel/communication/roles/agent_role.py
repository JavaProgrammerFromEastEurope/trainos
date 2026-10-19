from enum import Enum


class AgentRole(Enum):

    WORKER = "worker"
    LEADER = "leader"
    OBSERVER = "observer"
    COORDINATOR = "coordinator"

    def is_managerial(self) -> bool:
        return self in {
            AgentRole.LEADER,
            AgentRole.COORDINATOR,
        }