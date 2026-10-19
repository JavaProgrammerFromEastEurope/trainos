from .delegation_engine import DelegationEngine


class DelegationRuntime:

    def __init__(self) -> None:
        self._engine = DelegationEngine()

    def initialize(self) -> None:
        pass

    def update(self, delegation):
        return self._engine.delegate(delegation)

    def shutdown(self) -> None:
        pass
