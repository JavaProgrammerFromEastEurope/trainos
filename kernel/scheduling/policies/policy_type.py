from enum import Enum


class PolicyType(Enum):

    FIFO 				= "fifo"
    PRIORITY 		= "priority"
    ROUND_ROBIN = "round_robin"
    DEADLINE = "deadline"