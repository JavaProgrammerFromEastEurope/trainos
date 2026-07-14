from enum import Enum


class BusStatus(Enum):

    READY 			= "ready"
    DISPATCHING = "dispatching"
    STOPPED 		= "stopped"