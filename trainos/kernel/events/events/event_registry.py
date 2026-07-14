from kernel.core.registry.base_registry import BaseRegistry

from .event import Event


class EventRegistry(
    BaseRegistry[Event],
):
    pass
