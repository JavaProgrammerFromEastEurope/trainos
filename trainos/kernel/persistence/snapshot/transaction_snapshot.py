from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class TransactionSnapshot:

    active_transactions: int
