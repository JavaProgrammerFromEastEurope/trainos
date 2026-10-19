from enum import Enum


class RouteStatus(Enum):

    AVAILABLE 	= "available"
    BLOCKED 		= "blocked"
    MAINTENANCE = "maintenance"
    DISABLED 		= "disabled"