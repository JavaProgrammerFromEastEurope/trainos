from kernel.governance.deliberation.governance_deliberation import GovernanceDeliberation
from kernel.governance.deliberation.deliberation_status import DeliberationStatus

from kernel.governance.legitimacy.governance_legitimacy import GovernanceLegitimacy
from kernel.governance.legitimacy.legitimacy_status import LegitimacyStatus


def test_deliberation_legitimacy_flow():

    deliberation = GovernanceDeliberation(
        proposal="Increase resource allocation",
        status=DeliberationStatus.APPROVED,
    )

    legitimacy = GovernanceLegitimacy(
        proposal=deliberation.proposal,
        status=LegitimacyStatus.LEGITIMATE,
    )

    assert legitimacy.status == LegitimacyStatus.LEGITIMATE