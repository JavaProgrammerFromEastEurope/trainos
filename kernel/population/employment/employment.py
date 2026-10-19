from dataclasses import dataclass

from .employment_status import EmploymentStatus
from .employment_type 	import EmploymentType


@dataclass(frozen=True, slots=True)
class Employment:

    employment_id: 		str
    resident_id: 			str
    profession_id: 		str
    organization_id: 	str
    employment_type: EmploymentType
    status: EmploymentStatus