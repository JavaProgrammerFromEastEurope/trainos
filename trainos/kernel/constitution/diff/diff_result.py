from enum import Enum


class DiffResult(Enum):

    IDENTICAL 		= "identical"
    MODIFIED 			= "modified"
    INCOMPATIBLE 	= "incompatible"