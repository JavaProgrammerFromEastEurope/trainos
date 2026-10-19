from enum import Enum


class CognitiveState(Enum):

    IDLE 			= "idle"
    THINKING 	= "thinking"
    EXECUTING = "executing"
    PAUSED 		= "paused"