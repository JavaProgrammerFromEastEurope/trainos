from .governance_configuration import GovernanceConfiguration
from .governance_context 			import GovernanceContext
from .governance_scheduler 		import GovernanceScheduler


class GovernanceRuntime:

    def __init__(self) -> None:
        self._context = GovernanceContext(
            configuration=GovernanceConfiguration(),
        )
        self._scheduler = GovernanceScheduler()

    @property
    def context(self) -> GovernanceContext:
        return self._context

    def initialize(self) -> None:
        pass

    def update(self) -> None:
        self._scheduler.update(
            self._context,
        )

    def shutdown(self) -> None:
        pass
