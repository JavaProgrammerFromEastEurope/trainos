from dataclasses import dataclass

from .amendment_type import AmendmentType


@dataclass(frozen=True)
class AmendmentProposal:

    proposal_id: 			str
    target_article: 	str
    amendment: AmendmentType
    description: 			str