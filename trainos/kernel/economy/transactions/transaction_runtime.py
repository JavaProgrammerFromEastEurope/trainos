from .transaction_engine import TransactionEngine


class TransactionRuntime:

    def __init__(self) -> None:
        self._engine = TransactionEngine()

    def initialize(self) -> None:
        pass

    def update(self, transaction):
        return self._engine.validate(transaction)

    def shutdown(self) -> None:
        pass
