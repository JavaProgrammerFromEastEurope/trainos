from trainos.kernel.constitution.amendment.ratification.constitutional_ratification import ConstitutionalRatification
from trainos.kernel.constitution.amendment.ratification.ratification_result import RatificationResult


def test_constitutional_ratification():

    ratification = ConstitutionalRatification(
        proposal_id="A-001",
        result=RatificationResult.RATIFIED,
        authority="Constitutional Council",
    )

    assert ratification.result == RatificationResult.RATIFIED