from kernel.core.registry.base_registry import BaseRegistry

from .education_facility import EducationFacility


class EducationFacilityRegistry(
    BaseRegistry[EducationFacility],
):
    pass