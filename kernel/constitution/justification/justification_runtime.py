from .justification_engine import JustificationEngine


class JustificationRuntime:

    def __init__(self) -> None:
        self._engine = JustificationEngine()

    def initialize(self) -> None:
        pass

    def update(self, justification):
        return self._engine.justify(justification)

    def shutdown(self) -> None:
        pass
