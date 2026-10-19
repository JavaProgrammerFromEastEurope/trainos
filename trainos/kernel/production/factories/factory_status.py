from enum import Enum


class FactoryStatus(Enum):

    ACTIVE 			= "active"
    IDLE 				= "idle"
    MAINTENANCE = "maintenance"
    OFFLINE = "offline"