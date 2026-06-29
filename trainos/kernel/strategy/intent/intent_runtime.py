from .intent_engine import IntentEngine


class IntentRuntime:

    def __init__(self) -> None:
        self._engine = IntentEngine()

    def initialize(self) -> None:
        pass

    def update(self, intent):
        return self._engine.synthesize(intent)

    def shutdown(self) -> None:
        pass
