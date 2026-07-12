from dataclasses import dataclass

from kernel.governance.offices.governance_office_status import GovernanceOfficeStatus


@dataclass(frozen=True, slots=True)
class GovernanceOfficeSnapshot:

    office_id: str
    status: GovernanceOfficeStatus
