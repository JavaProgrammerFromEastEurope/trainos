from .guardian_engine import GuardianEngine


class GuardianRuntime:

    def __init__(self) -> None:
        self._engine = GuardianEngine()

    def initialize(self) -> None:
        pass

    def update(self, guardian):
        return self._engine.protect(guardian)

    def shutdown(self) -> None:
        pass
