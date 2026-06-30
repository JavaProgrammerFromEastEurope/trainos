from .legitimacy_engine import LegitimacyEngine


class LegitimacyRuntime:

    def __init__(self) -> None:
        self._engine = LegitimacyEngine()

    def initialize(self) -> None:
        pass

    def update(self, legitimacy):
        return self._engine.validate(legitimacy)

    def shutdown(self) -> None:
        pass
