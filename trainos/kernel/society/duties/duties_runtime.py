from .duties_engine import DutiesEngine


class DutiesRuntime:

    def __init__(self) -> None:
        self._engine = DutiesEngine()

    def initialize(self) -> None:
        pass

    def update(self, duties):
        return self._engine.evaluate(duties)

    def shutdown(self) -> None:
        pass
