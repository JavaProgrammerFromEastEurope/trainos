from enum import Enum


class TransactionOperation(Enum):

    SAVE 		= "save"
    UPDATE 	= "update"
    DELETE 	= "delete"