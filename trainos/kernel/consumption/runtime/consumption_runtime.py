from .consumption_configuration import ConsumptionConfiguration
from .consumption_context import ConsumptionContext
from .consumption_scheduler import ConsumptionScheduler


class ConsumptionRuntime:

    def __init__(self) -> None:
        self._context = ConsumptionContext(
            configuration=ConsumptionConfiguration(),
        )
        self._scheduler = ConsumptionScheduler()

    @property
    def context(self) -> ConsumptionContext:
        return self._context

    def initialize(self) -> None:
        pass

    def update(self) -> None:
        self._scheduler.update(self._context)

    def shutdown(self) -> None:
        pass
