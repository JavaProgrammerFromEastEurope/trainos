from enum import Enum


class TransactionType(Enum):

    TRANSFER 		= "transfer"
    DEPOSIT 		= "deposit"
    WITHDRAW 		= "withdraw"
    TAX 				= "tax"
    SALARY 			= "salary"
    REWARD 			= "reward"
    FINE 				= "fine"
    GRANT = "grant"