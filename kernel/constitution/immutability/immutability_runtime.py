from .immutability_engine import ImmutabilityEngine


class ImmutabilityRuntime:

    def __init__(self) -> None:
        self._engine = ImmutabilityEngine()

    def initialize(self) -> None:
        pass

    def update(self, entry):
        return self._engine.classify(entry)

    def shutdown(self) -> None:
        pass
