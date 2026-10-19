from .institution_registry import InstitutionRegistry
from .institution_registry_engine import InstitutionRegistryEngine


class InstitutionRegistryRuntime:

    def __init__(self) -> None:
        self._registry = InstitutionRegistry()
        self._engine = InstitutionRegistryEngine(self._registry)

    @property
    def registry(self) -> InstitutionRegistry:
        return self._registry

    def initialize(self) -> None:
        pass

    def update(self, institution):
        return self._engine.register(institution)

    def shutdown(self) -> None:
        pass
