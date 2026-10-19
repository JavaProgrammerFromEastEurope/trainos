from dataclasses import dataclass

from .review_result import ReviewResult


@dataclass(frozen=True)
class ConstitutionalReview:

    proposal_id: str
    result: ReviewResult
    notes: str