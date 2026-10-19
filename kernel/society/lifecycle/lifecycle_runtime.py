from .lifecycle_engine import LifecycleEngine


class LifecycleRuntime:

    def __init__(self) -> None:
        self._engine = LifecycleEngine()

    def initialize(self) -> None:
        pass

    def update(self, lifecycle):
        return self._engine.transition(lifecycle)

    def shutdown(self) -> None:
        pass
