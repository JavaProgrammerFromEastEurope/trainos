from .resources_context import ResourcesContext
from .resources_engine import ResourcesEngine
from .resources_configuration import ResourcesConfiguration


class ResourcesRuntime:

    def __init__(self) -> None:
        self._context = ResourcesContext(
            configuration=ResourcesConfiguration(),
        )
        self._engine = ResourcesEngine()

    @property
    def context(self) -> ResourcesContext:
        return self._context

    def initialize(self) -> None:
        self._engine.initialize(self._context)

    def update(self) -> None:
        self._engine.update(self._context)

    def shutdown(self) -> None:
        self._engine.shutdown(self._context)
