from kernel.core.registry.base_registry import BaseRegistry

from .message_bus import MessageBus


class MessageBusRegistry(
    BaseRegistry[MessageBus],
):
    pass
