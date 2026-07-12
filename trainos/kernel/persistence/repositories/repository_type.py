from enum import Enum


class RepositoryType(Enum):

    MEMORY 		= "memory"
    DATABASE 	= "database"
    FILE 			= "file"