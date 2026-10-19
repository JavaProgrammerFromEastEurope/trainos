from kernel.core.registry.base_registry import BaseRegistry

from .healthcare_definition import HealthcareDefinition


class HealthcareRegistry(
    BaseRegistry[HealthcareDefinition],
):
    pass
