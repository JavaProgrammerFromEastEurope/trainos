from dataclasses import dataclass

from .healthcare_category import HealthcareCategory
from .healthcare_type import HealthcareType


@dataclass(frozen=True, slots=True)
class HealthcareDefinition:

    healthcare_id: 	str
    name: 					str
    healthcare_type: HealthcareType
    category: HealthcareCategory