from dataclasses import dataclass


@dataclass(frozen=True)
class TransactionPolicy:

    immutable_transactions: bool
    allow_negative_amount: 	bool