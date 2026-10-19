from enum import Enum


class PublisherStatus(Enum):

    READY 			= "ready"
    PUBLISHING 	= "publishing"
    STOPPED 		= "stopped"