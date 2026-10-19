from .institution_lifecycle_engine import InstitutionLifecycleEngine


class InstitutionLifecycleRuntime:

    def __init__(self) -> None:
        self._engine = InstitutionLifecycleEngine()

    def initialize(self) -> None:
        pass

    def update(self, lifecycle):
        return self._engine.update(lifecycle)

    def shutdown(self) -> None:
        pass
