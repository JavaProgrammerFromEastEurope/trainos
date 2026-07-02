from trainos.kernel.constitution.amendment.amendment_proposal import AmendmentProposal
from trainos.kernel.constitution.amendment.amendment_type import AmendmentType


def test_amendment_proposal_creation():

    proposal = AmendmentProposal(
        proposal_id="A-001",
        target_article="Article 5",
        amendment=AmendmentType.MODIFICATION,
        description="Clarify emergency governance",
    )

    assert proposal.proposal_id == "A-001"
    assert proposal.amendment == AmendmentType.MODIFICATION