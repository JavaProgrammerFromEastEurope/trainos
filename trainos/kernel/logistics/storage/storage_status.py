from enum import Enum


class StorageStatus(Enum):

    AVAILABLE = "available"
    RESERVED 	= "reserved"
    LOCKED 		= "locked"
    DAMAGED 	= "damaged"