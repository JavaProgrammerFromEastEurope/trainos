from kernel.core.registry.base_registry import BaseRegistry

from .security_definition import SecurityDefinition


class SecurityRegistry(
    BaseRegistry[SecurityDefinition],
):
    pass
