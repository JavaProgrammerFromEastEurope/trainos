from enum import Enum


class IdentityRole(Enum):

    CITIZEN 	= "citizen"
    RESIDENT 	= "resident"
    VISITOR 	= "visitor"
    WORKER 		= "worker"
    OFFICIAL 	= "official"
    AI_AGENT 	= "ai_agent"