from .currency_engine import CurrencyEngine


class CurrencyRuntime:

    def __init__(self) -> None:
        self._engine = CurrencyEngine()

    def initialize(self) -> None:
        pass

    def update(self, currency):
        return self._engine.validate(currency)

    def shutdown(self) -> None:
        pass
