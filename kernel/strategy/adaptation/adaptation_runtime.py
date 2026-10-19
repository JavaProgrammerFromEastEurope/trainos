from .adaptation_engine import AdaptationEngine


class AdaptationRuntime:

    def __init__(self) -> None:
        self._engine = AdaptationEngine()

    def initialize(self) -> None:
        pass

    def update(self, strategy):
        return self._engine.adapt(strategy)

    def shutdown(self) -> None:
        pass
