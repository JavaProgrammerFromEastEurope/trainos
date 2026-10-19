from .governance_engine import GovernanceEngine


class GovernanceRuntime:

    def __init__(self) -> None:
        self._engine = GovernanceEngine()

    def initialize(self) -> None:
        pass

    def update(self, authority):
        return self._engine.authorize(authority)

    def shutdown(self) -> None:
        pass
