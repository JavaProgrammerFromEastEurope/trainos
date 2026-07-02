from trainos.kernel.constitution.amendment.amendment_registry import AmendmentRegistry
from trainos.kernel.constitution.amendment.amendment_proposal import AmendmentProposal
from trainos.kernel.constitution.amendment.amendment_type import AmendmentType


def test_amendment_registry():

    registry = AmendmentRegistry()

    registry.register(
        AmendmentProposal(
            proposal_id="A-001",
            target_article="Article 3",
            amendment=AmendmentType.ADDITION,
            description="Add constitutional safeguard",
        )
    )

    assert len(registry.proposals()) == 1