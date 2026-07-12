from enum import Enum


class TransactionStatus(Enum):

    CREATED 	= "created"
    ACTIVE 		= "active"
    COMMITTED = "committed"
    ROLLED_BACK = "rolled_back"