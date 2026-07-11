from kernel.core.registry.base_registry import BaseRegistry

from .security_facility import SecurityFacility


class SecurityFacilityRegistry(
    BaseRegistry[SecurityFacility],
):
    pass
