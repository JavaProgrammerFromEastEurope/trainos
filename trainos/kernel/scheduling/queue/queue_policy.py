from enum import Enum


class QueuePolicy(Enum):

    FIFO 			= "fifo"
    PRIORITY 	= "priority"