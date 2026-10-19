from kernel.core.registry.base_registry import BaseRegistry

from .integration_event import IntegrationEvent


class IntegrationEventRegistry(
    BaseRegistry[IntegrationEvent],
):
    pass
