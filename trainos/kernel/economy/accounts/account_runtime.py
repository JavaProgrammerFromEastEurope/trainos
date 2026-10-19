from .account_engine import AccountEngine


class AccountRuntime:

    def __init__(self) -> None:
        self._engine = AccountEngine()

    def initialize(self) -> None:
        pass

    def update(self, account):
        return self._engine.validate(account)

    def shutdown(self) -> None:
        pass
