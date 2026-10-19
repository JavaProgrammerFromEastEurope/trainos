from dataclasses import dataclass

from .transaction_status import TransactionStatus


@dataclass(frozen=True, slots=True)
class Transaction:

    transaction_id: str
    status: TransactionStatus