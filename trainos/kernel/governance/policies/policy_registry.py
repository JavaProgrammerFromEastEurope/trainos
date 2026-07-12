from kernel.core.registry.base_registry import BaseRegistry

from .policy import Policy


class PolicyRegistry(
    BaseRegistry[Policy],
):
    pass
