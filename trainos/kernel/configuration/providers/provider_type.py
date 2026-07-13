from enum import Enum


class ProviderType(Enum):

    DEFAULT 	= "default"
    FILE 			= "file"
    DATABASE 	= "database"
    ENVIRONMENT = "environment"