from enum import Enum


class EntityType(Enum):

    UNKNOWN 	= "unknown"
    OBJECT 		= "object"
    HUMAN 		= "human"
    DRONE 		= "drone"
    VEHICLE 	= "vehicle"
    BUILDING 	= "building"
    TARGET 		= "target"
    SENSOR 		= "sensor"