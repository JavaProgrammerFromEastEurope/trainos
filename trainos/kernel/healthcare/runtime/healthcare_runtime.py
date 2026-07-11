from .healthcare_configuration import HealthcareConfiguration
from .healthcare_context import HealthcareContext
from .healthcare_scheduler import HealthcareScheduler


class HealthcareRuntime:

    def __init__(self) -> None:
        self._context = HealthcareContext(
            configuration=HealthcareConfiguration(),
        )
        self._scheduler = HealthcareScheduler()

    @property
    def context(self) -> HealthcareContext:
        return self._context

    def initialize(self) -> None:
        pass

    def update(self) -> None:
        self._scheduler.update(
            self._context,
        )

    def shutdown(self) -> None:
        pass
