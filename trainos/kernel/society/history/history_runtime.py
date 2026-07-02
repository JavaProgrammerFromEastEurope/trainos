from .history_engine import HistoryEngine


class HistoryRuntime:

    def __init__(self) -> None:
        self._engine = HistoryEngine()

    def initialize(self) -> None:
        pass

    def update(self, entry):
        return self._engine.append(entry)

    def shutdown(self) -> None:
        pass
