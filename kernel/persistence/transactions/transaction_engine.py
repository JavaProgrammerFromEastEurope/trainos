from .transaction_manager import TransactionManager


class TransactionEngine:

    def __init__(self):
        self.manager = TransactionManager()

    def start(self, transaction_id):
        return self.manager.begin(transaction_id)

    def commit(self, transaction):
        return self.manager.commit(transaction)

    def rollback(self, transaction):
        return self.manager.rollback(transaction)
