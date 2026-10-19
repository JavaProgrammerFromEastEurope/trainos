from .rollback_engine import RollbackEngine


class RollbackRuntime:

    def __init__(self) -> None:
        self._engine = RollbackEngine()

    def initialize(self) -> None:
        pass

    def update(self, rollback):
        return self._engine.rollback(rollback)

    def shutdown(self) -> None:
        pass
