from enum import Enum


class ConsumerStatus(Enum):

    ACTIVE 	= "active"
    PAUSED 	= "paused"
    OFFLINE = "offline"