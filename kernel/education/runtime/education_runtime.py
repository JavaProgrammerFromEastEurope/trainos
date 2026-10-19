from .education_configuration import EducationConfiguration
from .education_context import EducationContext
from .education_scheduler import EducationScheduler


class EducationRuntime:

    def __init__(self) -> None:
        self._context = EducationContext(
            configuration=EducationConfiguration(),
        )
        self._scheduler = EducationScheduler()

    @property
    def context(self) -> EducationContext:
        return self._context

    def initialize(self) -> None:
        pass

    def update(self) -> None:
        self._scheduler.update(self._context)

    def shutdown(self) -> None:
        pass
