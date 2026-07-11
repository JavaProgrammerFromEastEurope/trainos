from dataclasses import dataclass

from .healthcare_facility_status 	import HealthcareFacilityStatus
from .healthcare_facility_type 		import HealthcareFacilityType


@dataclass(frozen=True, slots=True)
class HealthcareFacility:

    facility_id: 	str
    name: 				str
    facility_type: HealthcareFacilityType
    status: HealthcareFacilityStatus