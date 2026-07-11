from kernel.core.registry.base_registry import BaseRegistry

from .security_patrol import SecurityPatrol


class SecurityPatrolRegistry(
    BaseRegistry[SecurityPatrol],
):
    pass
