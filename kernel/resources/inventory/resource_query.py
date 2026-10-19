from .resource_registry import ResourceRegistry


class ResourceQuery:

    def get(self, registry: ResourceRegistry, resource_id: str):
        return registry.get(resource_id)

    def all(self, registry: ResourceRegistry):
        return registry.all()

    def exists(self, registry: ResourceRegistry, resource_id: str) -> bool:
        return registry.exists(resource_id)