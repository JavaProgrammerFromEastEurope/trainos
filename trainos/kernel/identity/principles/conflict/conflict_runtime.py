from .conflict_engine import PrincipleConflictEngine


class PrincipleConflictRuntime:

    def __init__(self) -> None:
        self._engine = PrincipleConflictEngine()

    def initialize(self) -> None:
        pass

    def update(self, conflict):
        return self._engine.resolve(conflict)

    def shutdown(self) -> None:
        pass
