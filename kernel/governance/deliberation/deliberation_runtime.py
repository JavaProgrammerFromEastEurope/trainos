from .deliberation_engine import DeliberationEngine


class DeliberationRuntime:

    def __init__(self) -> None:
        self._engine = DeliberationEngine()

    def initialize(self) -> None:
        pass

    def update(self, deliberation):
        return self._engine.deliberate(deliberation)

    def shutdown(self) -> None:
        pass
