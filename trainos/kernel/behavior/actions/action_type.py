from enum import Enum


class ActionType(Enum):

    UNKNOWN 	= "unknown"
    MOVE 			= "move"
    ROTATE 		= "rotate"
    OBSERVE 	= "observe"
    SCAN 			= "scan"
    ATTACK 		= "attack"
    COLLECT 	= "collect"
    RECHARGE 	= "recharge"
    WAIT 			= "wait"
    COMMUNICATE = "communicate"