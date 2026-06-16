from enum import Enum


class TaskType(Enum):

    UNKNOWN 	= "unknown"
    ROOT 			= "root"
    SEQUENCE 	= "sequence"
    SELECTOR 	= "selector"
    LEAF 			= "leaf"