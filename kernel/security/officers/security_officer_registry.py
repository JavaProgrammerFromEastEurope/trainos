from kernel.core.registry.base_registry import BaseRegistry

from .security_officer import SecurityOfficer


class SecurityOfficerRegistry(
    BaseRegistry[SecurityOfficer],
):
    pass
