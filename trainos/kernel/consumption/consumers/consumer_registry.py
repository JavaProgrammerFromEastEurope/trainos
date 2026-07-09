from kernel.core.registry.base_registry import BaseRegistry

from .consumer import Consumer


class ConsumerRegistry(
    BaseRegistry[Consumer],
):
    pass
