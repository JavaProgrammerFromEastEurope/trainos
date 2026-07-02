from .institution_history_engine import InstitutionHistoryEngine


class InstitutionHistoryRuntime:

    def __init__(self) -> None:
        self._engine = InstitutionHistoryEngine()

    def initialize(self) -> None:
        pass

    def update(self, entry):
        return self._engine.append(entry)

    def shutdown(self) -> None:
        pass
