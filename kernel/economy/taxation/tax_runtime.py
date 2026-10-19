from .tax_engine import TaxEngine


class TaxRuntime:

    def __init__(self) -> None:
        self._engine = TaxEngine()

    def initialize(self) -> None:
        pass

    def update(self, *args, **kwargs):
        return self._engine.calculate(*args, **kwargs)

    def shutdown(self) -> None:
        pass
