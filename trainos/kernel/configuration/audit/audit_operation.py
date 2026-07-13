from enum import Enum


class AuditOperation(Enum):

    CREATE = "create"
    UPDATE = "update"
    DELETE = "delete"
    LOAD = "load"