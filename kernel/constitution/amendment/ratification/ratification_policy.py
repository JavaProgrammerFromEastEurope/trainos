from dataclasses import dataclass


@dataclass(frozen=True)
class RatificationPolicy:

    require_review_completion: bool
    require_authority: bool