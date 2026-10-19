from dataclasses import dataclass

from .resident_status import ResidentStatus
from .resident_type import ResidentType


@dataclass(frozen=True, slots=True)
class Resident:

    resident_id: 	str
    name: 				str
    resident_type: ResidentType
    status: ResidentStatus