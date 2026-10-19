from .base_context import BaseContext
from .base_engine import BaseEngine
from .lifecycle_state import LifecycleState


class BaseRuntime:

    def __init__(self, engine: BaseEngine) -> None:
        self._context = BaseContext()
        self._engine = engine

    def initialize(self) -> None:
        self._engine.initialize(self._context)
        self._context.lifecycle.transition(LifecycleState.INITIALIZED)

    def start(self) -> None:
        self._context.lifecycle.transition(LifecycleState.RUNNING)

    def update(self, *args, **kwargs) -> None:
        self._engine.update(self._context, *args, **kwargs)

    def stop(self) -> None:
        self._context.lifecycle.transition(LifecycleState.STOPPED)

    def shutdown(self) -> None:
        self._engine.shutdown(self._context)
        self._context.lifecycle.transition(LifecycleState.SHUTDOWN)

    @property
    def context(self) -> BaseContext:
        return self._context
