from enum import Enum


class WarehouseStatus(Enum):

    ACTIVE 			= "active"
    FULL 				= "full"
    MAINTENANCE = "maintenance"
    OFFLINE = "offline"