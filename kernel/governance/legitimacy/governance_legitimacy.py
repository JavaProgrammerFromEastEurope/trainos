from dataclasses import dataclass

from .legitimacy_status import LegitimacyStatus


@dataclass(frozen=True)
class GovernanceLegitimacy:

    proposal: str
    status: LegitimacyStatus
