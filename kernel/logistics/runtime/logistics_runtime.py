from .logistics_configuration import LogisticsConfiguration
from .logistics_context import LogisticsContext
from .logistics_scheduler import LogisticsScheduler


class LogisticsRuntime:

    def __init__(self) -> None:
        self._context = LogisticsContext(
            configuration=LogisticsConfiguration(),
        )
        self._scheduler = LogisticsScheduler()

    @property
    def context(self) -> LogisticsContext:
        return self._context

    def initialize(self) -> None:
        pass

    def update(self) -> None:
        self._scheduler.update(self._context)

    def shutdown(self) -> None:
        pass
