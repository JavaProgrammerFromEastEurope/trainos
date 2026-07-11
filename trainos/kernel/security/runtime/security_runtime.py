from .security_context import SecurityContext
from .security_configuration import SecurityConfiguration
from .security_scheduler import SecurityScheduler


class SecurityRuntime:

    def __init__(self) -> None:
        self._context = SecurityContext(
            configuration=SecurityConfiguration(),
        )
        self._scheduler = SecurityScheduler()

    @property
    def context(self) -> SecurityContext:
        return self._context

    def initialize(self) -> None:
        pass

    def update(self) -> None:
        self._scheduler.update(
            self._context,
        )

    def shutdown(self) -> None:
        pass
