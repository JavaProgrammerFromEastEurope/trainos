from enum import Enum


class MessageType(Enum):

    TEXT 		= "text"
    SIGNAL 	= "signal"
    COMMAND = "command"