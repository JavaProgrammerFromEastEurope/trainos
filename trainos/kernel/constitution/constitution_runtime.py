from .constitution_engine import ConstitutionEngine


class ConstitutionRuntime:

    def __init__(self) -> None:
        self._engine = ConstitutionEngine()

    def initialize(self) -> None:
        pass

    def update(self, rule):
        return self._engine.evaluate(rule)

    def shutdown(self) -> None:
        pass
