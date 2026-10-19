from dataclasses import dataclass

from .deliberation_status import DeliberationStatus


@dataclass(frozen=True)
class GovernanceDeliberation:

    proposal: str
    status: DeliberationStatus