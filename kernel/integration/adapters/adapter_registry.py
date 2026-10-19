from kernel.core.registry.base_registry import BaseRegistry

from .integration_adapter import IntegrationAdapter


class AdapterRegistry(
    BaseRegistry[IntegrationAdapter]
):
    pass