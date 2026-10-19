from kernel.core.registry.base_registry import BaseRegistry

from .publisher import Publisher


class PublisherRegistry(
    BaseRegistry[Publisher],
):
    pass
