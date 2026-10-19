from .institution import Institution
from .institution_registry import InstitutionRegistry


class InstitutionRegistryEngine:

    def __init__(self, registry: InstitutionRegistry) -> None:
        self._registry = registry

    def register(self, institution: Institution) -> Institution:
        self._registry.register(institution)
        return institution
