from .value_engine import ValueEngine


class ValueRuntime:

    def __init__(self) -> None:
        self._engine = ValueEngine()

    def initialize(self) -> None:
        pass

    def update(self, outcome):
        return self._engine.evaluate(outcome)

    def shutdown(self) -> None:
        pass
