from enum import Enum


class StorageStatus(Enum):

    CREATED 			= "created"
    INITIALIZING 	= "initializing"
    RUNNING 			= "running"
    PAUSED 				= "paused"
    STOPPED 			= "stopped"