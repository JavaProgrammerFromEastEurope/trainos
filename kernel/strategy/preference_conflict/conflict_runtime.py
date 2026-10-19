from .conflict_engine import ConflictEngine


class ConflictRuntime:

    def __init__(self) -> None:
        self._engine = ConflictEngine()

    def initialize(self) -> None:
        pass

    def update(self, pair):
        return self._engine.resolve(pair)

    def shutdown(self) -> None:
        pass
