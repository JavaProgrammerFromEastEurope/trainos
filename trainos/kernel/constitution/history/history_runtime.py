from .history_engine import HistoryEngine


class HistoryRuntime:

    def __init__(self) -> None:
        self._engine = HistoryEngine()

    def initialize(self) -> None:
        pass

    def update(self, history):
        return self._engine.snapshot(history)

    def shutdown(self) -> None:
        pass
