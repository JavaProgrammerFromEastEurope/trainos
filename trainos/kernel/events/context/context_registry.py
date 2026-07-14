from kernel.core.registry.base_registry import BaseRegistry

from .event_context import EventContext


class ContextRegistry(
    BaseRegistry[EventContext],
):
    pass
