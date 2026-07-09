from .population_configuration import PopulationConfiguration
from .population_context 		import PopulationContext
from .population_scheduler 	import PopulationScheduler


class PopulationRuntime:

    def __init__(self) -> None:
        self._context = PopulationContext(
            configuration=PopulationConfiguration(),
        )
        self._scheduler = PopulationScheduler()

    @property
    def context(self) -> PopulationContext:
        return self._context

    def initialize(self) -> None:
        pass

    def update(self) -> None:
        self._scheduler.update(
            self._context,
        )

    def shutdown(self) -> None:
        pass
