from kernel.core.registry.base_registry import BaseRegistry

from .subscriber import Subscriber


class SubscriberRegistry(
    BaseRegistry[Subscriber],
):
    pass