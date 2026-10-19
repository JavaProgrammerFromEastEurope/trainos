from .production_configuration import ProductionConfiguration
from .production_context import ProductionContext
from .production_scheduler import ProductionScheduler


class ProductionRuntime:

    def __init__(self) -> None:
        self._context = ProductionContext(
            configuration=ProductionConfiguration(),
        )
        self._scheduler = ProductionScheduler()

    @property
    def context(self) -> ProductionContext:
        return self._context

    def initialize(self) -> None:
        pass

    def update(self) -> None:
        self._scheduler.update(self._context)

    def shutdown(self) -> None:
        pass
