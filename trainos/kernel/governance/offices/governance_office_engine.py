from .governance_office import GovernanceOffice
from .governance_office_status import GovernanceOfficeStatus


class GovernanceOfficeEngine:

    def open(
        self,
        office: GovernanceOffice,
    ) -> GovernanceOffice:

        return GovernanceOffice(
            office_id=office.office_id,
            name=office.name,
            office_type=office.office_type,
            status=GovernanceOfficeStatus.OPERATIONAL,
        )

    def close(
        self,
        office: GovernanceOffice,
    ) -> GovernanceOffice:

        return GovernanceOffice(
            office_id=office.office_id,
            name=office.name,
            office_type=office.office_type,
            status=GovernanceOfficeStatus.CLOSED,
        )