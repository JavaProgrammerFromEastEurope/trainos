from kernel.governance.offices.governance_office import GovernanceOffice
from kernel.governance.offices.governance_office_engine import GovernanceOfficeEngine
from kernel.governance.offices.governance_office_status import GovernanceOfficeStatus
from kernel.governance.offices.governance_office_type import GovernanceOfficeType


def test_governance_office_engine():

    engine = GovernanceOfficeEngine()
    office = GovernanceOffice(
        office_id="O1",
        name="Central Office",
        office_type=GovernanceOfficeType.ADMINISTRATION,
        status=GovernanceOfficeStatus.CLOSED,
    )

    opened = engine.open(office)
    assert opened.status == GovernanceOfficeStatus.OPERATIONAL

    closed = engine.close(opened)
    assert closed.status == GovernanceOfficeStatus.CLOSED
