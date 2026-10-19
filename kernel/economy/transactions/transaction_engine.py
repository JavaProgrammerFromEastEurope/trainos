from .transaction import Transaction


class TransactionEngine:

    def validate(
        self,
        transaction: Transaction,
    ) -> Transaction:
        return transaction
