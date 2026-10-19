from .economy_context import EconomyContext
from .economy_engine 	import EconomyEngine


class EconomyRuntime:

    def __init__(self) -> None:
        self._context = EconomyContext()
        self._engine 	= EconomyEngine()

    def initialize(self) -> None:
        self._engine.initialize(self._context)

    def start(self) -> None:
        self._engine.start(self._context)

    def shutdown(self) -> None:
        self._engine.stop(self._context)

    @property
    def context(self):
        return self._context
