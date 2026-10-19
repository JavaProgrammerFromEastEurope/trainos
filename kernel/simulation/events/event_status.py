from enum import Enum


class EventStatus(Enum):

    CREATED 	= "created"
    PROCESSED = "processed"
    FAILED 		= "failed"