from __future__ import annotations

from .transaction import Transaction


class TransactionRegistry:

    def __init__(self) -> None:
        self._transactions: list[Transaction] = []

    def register(
        self,
        transaction: Transaction,
    ) -> None:
        self._transactions.append(transaction)

    def all(self) -> tuple[Transaction, ...]:
        return tuple(self._transactions)
