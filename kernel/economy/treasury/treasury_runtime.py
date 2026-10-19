from .treasury_engine import TreasuryEngine


class TreasuryRuntime:

    def __init__(self) -> None:
        self._engine = TreasuryEngine()

    def initialize(self) -> None:
        pass

    def update(self, treasury):
        return self._engine.validate(treasury)

    def shutdown(self) -> None:
        pass
