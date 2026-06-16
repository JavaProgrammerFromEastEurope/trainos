from enum import Enum


class AgentRole(Enum):

    LEADER 		= "leader"
    FOLLOWER 	= "follower"
    OBSERVER 	= "observer"
    UNKNOWN 	= "unknown"