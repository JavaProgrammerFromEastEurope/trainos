from enum import Enum


class MessageStatus(Enum):

    CREATED 	= "created"
    QUEUED 		= "queued"
    DELIVERED = "delivered"