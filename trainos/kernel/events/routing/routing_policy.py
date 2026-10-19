from enum import Enum


class RoutingPolicy(Enum):

    BY_NAME 		= "by_name"
    BY_PRIORITY = "by_priority"
    BROADCAST 	= "broadcast"