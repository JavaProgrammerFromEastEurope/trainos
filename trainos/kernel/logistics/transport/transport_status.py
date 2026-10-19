from enum import Enum


class TransportStatus(Enum):

    AVAILABLE 	= "available"
    BUSY 				= "busy"
    MAINTENANCE = "maintenance"
    OFFLINE = "offline"