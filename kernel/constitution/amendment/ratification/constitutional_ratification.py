from dataclasses import dataclass

from .ratification_result import RatificationResult


@dataclass(frozen=True)
class ConstitutionalRatification:

    proposal_id: str
    result: RatificationResult
    authority: str
