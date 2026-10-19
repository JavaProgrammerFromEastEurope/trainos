from dataclasses import dataclass


@dataclass(frozen=True)
class ReviewPolicy:

    require_written_feedback: bool
    require_completed_review: bool