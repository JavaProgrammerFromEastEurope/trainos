from enum import Enum


class PersistenceType(Enum):

    ENTITY 			= "entity"
    VALUE_OBJECT = "value_object"
    SNAPSHOT 		= "snapshot"
    HISTORY 		= "history"
    AUDIT 			= "audit"