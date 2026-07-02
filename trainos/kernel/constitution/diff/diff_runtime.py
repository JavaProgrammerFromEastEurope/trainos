from .diff_engine import DiffEngine


class DiffRuntime:

    def __init__(self) -> None:
        self._engine = DiffEngine()

    def initialize(self) -> None:
        pass

    def update(self, diff):
        return self._engine.compare(diff)

    def shutdown(self) -> None:
        pass
