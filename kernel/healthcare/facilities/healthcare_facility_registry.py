from kernel.core.registry.base_registry import BaseRegistry

from .healthcare_facility import HealthcareFacility


class HealthcareFacilityRegistry(
    BaseRegistry[HealthcareFacility],
):
    pass
