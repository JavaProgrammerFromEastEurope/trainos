from enum import Enum


class AuditOperation(Enum):

    CREATE 	= "create"
    READ 		= "read"
    UPDATE 	= "update"
    DELETE 	= "delete"
    RESTORE = "restore"