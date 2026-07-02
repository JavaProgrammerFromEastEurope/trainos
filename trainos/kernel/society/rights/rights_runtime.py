from .rights_engine import RightsEngine


class RightsRuntime:

    def __init__(self) -> None:
        self._engine = RightsEngine()

    def initialize(self) -> None:
        pass

    def update(self, rights):
        return self._engine.evaluate(rights)

    def shutdown(self) -> None:
        pass
