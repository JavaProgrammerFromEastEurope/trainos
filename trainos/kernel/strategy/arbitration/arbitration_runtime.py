from .arbitration_engine import ArbitrationEngine


class ArbitrationRuntime:

    def __init__(self) -> None:
        self._engine = ArbitrationEngine()

    def initialize(self) -> None:
        pass

    def update(self, conflict):
        return self._engine.resolve(conflict)

    def shutdown(self) -> None:
        pass
