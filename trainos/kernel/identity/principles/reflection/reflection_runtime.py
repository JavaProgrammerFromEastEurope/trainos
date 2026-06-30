from .reflection_engine import ReflectionEngine


class ReflectionRuntime:

    def __init__(self) -> None:
        self._engine = ReflectionEngine()

    def initialize(self) -> None:
        pass

    def update(self, reflection):
        return self._engine.reflect(reflection)

    def shutdown(self) -> None:
        pass
