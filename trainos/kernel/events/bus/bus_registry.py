from kernel.core.registry.base_registry import BaseRegistry

from .event_bus import EventBus


class BusRegistry(
    BaseRegistry[EventBus],
):
    pass
