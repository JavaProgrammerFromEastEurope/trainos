from kernel.core.registry.base_registry import BaseRegistry

from .integration_route import IntegrationRoute


class RouteRegistry(
    BaseRegistry[IntegrationRoute],
):
    pass
