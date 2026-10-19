from .intelligence_runtime_engine import IntelligenceRuntimeEngine


class IntelligenceRuntime:

    def __init__(self) -> None:
        self._engine = IntelligenceRuntimeEngine()
        self._initialized = False

    def initialize(self) -> None:
        self._initialized = True

    def update(self):
        if not self._initialized:
            raise RuntimeError("Runtime is not initialized.")
        return self._engine.next_cycle()

    def shutdown(self) -> None:
        self._initialized = False
