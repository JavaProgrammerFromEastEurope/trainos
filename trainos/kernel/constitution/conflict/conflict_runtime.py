from .conflict_engine import ConstitutionalConflictEngine


class ConstitutionalConflictRuntime:

    def __init__(self) -> None:
        self._engine = ConstitutionalConflictEngine()

    def initialize(self) -> None:
        pass

    def update(self, conflict):
        return self._engine.resolve(conflict)

    def shutdown(self) -> None:
        pass
