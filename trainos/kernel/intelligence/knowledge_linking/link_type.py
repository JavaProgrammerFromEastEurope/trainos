from enum import Enum


class LinkType(Enum):

    CAUSES 			= "causes"
    SUPPORTS 		= "supports"
    CONTRADICTS = "contradicts"
    DEPENDS_ON 	= "depends_on"
    RELATED_TO 	= "related_to"