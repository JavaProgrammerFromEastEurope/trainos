from trainos.kernel.constitution.amendment.lifecycle.amendment_lifecycle import AmendmentLifecycle
from trainos.kernel.constitution.amendment.lifecycle.amendment_state import AmendmentState


def test_amendment_lifecycle():

    lifecycle = AmendmentLifecycle(
        proposal_id="A-001",
        state=AmendmentState.UNDER_REVIEW,
    )

    assert lifecycle.state == AmendmentState.UNDER_REVIEW