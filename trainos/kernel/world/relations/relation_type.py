from enum import Enum


class RelationType(Enum):

    PARENT 	= "parent"
    CHILD 	= "child"
    OWNER 	= "owner"
    GROUP 	= "group"
    TEAM 		= "team"
    LINK 		= "link"