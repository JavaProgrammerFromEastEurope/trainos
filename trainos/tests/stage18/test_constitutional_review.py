from trainos.kernel.constitution.amendment.review.constitutional_review import ConstitutionalReview
from trainos.kernel.constitution.amendment.review.review_result import ReviewResult


def test_constitutional_review():

    review = ConstitutionalReview(
        proposal_id="A-001",
        result=ReviewResult.ACCEPTED,
        notes="Constitutionally valid",
    )

    assert review.result == ReviewResult.ACCEPTED