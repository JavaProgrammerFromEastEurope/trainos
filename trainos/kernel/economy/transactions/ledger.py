from .transaction import Transaction


class Ledger:

    def __init__(self) -> None:
        self._entries: list[Transaction] = []

    def append(self, transaction: Transaction) -> None:
        self._entries.append(transaction)

    def entries(self):
        return tuple(self._entries)
