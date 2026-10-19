from dataclasses import dataclass

from .governance_office_status import GovernanceOfficeStatus
from .governance_office_type import GovernanceOfficeType


@dataclass(frozen=True, slots=True)
class GovernanceOffice:

    office_id: 	str
    name: 			str
    office_type: GovernanceOfficeType
    status: GovernanceOfficeStatus