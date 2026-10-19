from dataclasses import dataclass

from .healthcare_configuration import HealthcareConfiguration


@dataclass(slots=True)
class HealthcareContext:

    configuration: HealthcareConfiguration