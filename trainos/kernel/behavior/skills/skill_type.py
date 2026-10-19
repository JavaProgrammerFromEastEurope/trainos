from enum import Enum


class SkillType(Enum):

    UNKNOWN 	= "unknown"
    NAVIGATE 	= "navigate"
    EXPLORE 	= "explore"
    PATROL 		= "patrol"
    SEARCH 		= "search"
    FOLLOW 		= "follow"
    TRACK_TARGET = "track_target"
    DOCK 			= "dock"
    AVOID_OBSTACLE = "avoid_obstacle"