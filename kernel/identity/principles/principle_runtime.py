from .principle_engine import PrincipleEngine


class PrincipleRuntime:

    def __init__(self) -> None:
        self._engine = PrincipleEngine()

    def initialize(self) -> None:
        pass

    def update(self, principle):
        return self._engine.establish(principle)

    def shutdown(self) -> None:
        pass
