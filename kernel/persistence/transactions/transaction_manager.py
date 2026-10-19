from .transaction import Transaction

from .transaction_status import TransactionStatus


class TransactionManager:

    def begin(
        self,
        transaction_id: str,
    ) -> Transaction:
        return Transaction(
            transaction_id=transaction_id,
            status=TransactionStatus.ACTIVE,
        )

    def commit(
        self,
        transaction: Transaction,
    ) -> Transaction:
        return Transaction(
            transaction_id=transaction.transaction_id,
            status=TransactionStatus.COMMITTED,
        )

    def rollback(
        self,
        transaction: Transaction,
    ) -> Transaction:
        return Transaction(
            transaction_id=transaction.transaction_id,
            status=TransactionStatus.ROLLED_BACK,
        )
