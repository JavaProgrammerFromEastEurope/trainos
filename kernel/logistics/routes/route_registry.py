from kernel.core.registry.base_registry import BaseRegistry

from .route import Route


class RouteRegistry(
    BaseRegistry[Route],
):
    pass
