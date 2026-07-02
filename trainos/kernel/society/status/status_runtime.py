from .status_engine import StatusEngine


class StatusRuntime:

    def __init__(self) -> None:
        self._engine = StatusEngine()

    def initialize(self) -> None:
        pass

    def update(self, status):
        return self._engine.evaluate(status)

    def shutdown(self) -> None:
        pass
