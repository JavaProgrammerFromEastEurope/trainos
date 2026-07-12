from enum import Enum


class PersistenceOperation(Enum):

    SAVE = "save"
    LOAD = "load"
    DELETE = "delete"