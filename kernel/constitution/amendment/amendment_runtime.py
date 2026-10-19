from .amendment_engine import AmendmentEngine


class AmendmentRuntime:

    def __init__(self) -> None:
        self._engine = AmendmentEngine()

    def initialize(self) -> None:
        pass

    def update(self, proposal):
        return self._engine.submit(proposal)

    def shutdown(self) -> None:
        pass
