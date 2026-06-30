from .institution_engine import InstitutionEngine


class InstitutionRuntime:

    def __init__(self) -> None:
        self._engine = InstitutionEngine()

    def initialize(self) -> None:
        pass

    def update(self, institution):
        return self._engine.establish(institution)

    def shutdown(self) -> None:
        pass
