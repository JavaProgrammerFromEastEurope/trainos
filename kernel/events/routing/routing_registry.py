from kernel.core.registry.base_registry import BaseRegistry

from .event_route import EventRoute


class RoutingRegistry(
    BaseRegistry[EventRoute],
):
    pass
