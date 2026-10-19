from .ratification_engine import RatificationEngine


class RatificationRuntime:

    def __init__(self) -> None:
        self._engine = RatificationEngine()

    def initialize(self) -> None:
        pass

    def update(self, ratification):
        return self._engine.ratify(ratification)

    def shutdown(self) -> None:
        pass
