from kernel.core.registry.base_registry import BaseRegistry

from .integration_handler import IntegrationHandler


class HandlerRegistry(
    BaseRegistry[IntegrationHandler],
):
    pass
