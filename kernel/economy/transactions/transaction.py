from dataclasses import dataclass
from decimal import Decimal

from .transaction_type import TransactionType


@dataclass(frozen=True)
class Transaction:

    transaction_id: 	str
    from_account: 		str | None
    to_account: 			str | None
    amount: 					Decimal
    currency_id: 			str
    transaction_type: TransactionType