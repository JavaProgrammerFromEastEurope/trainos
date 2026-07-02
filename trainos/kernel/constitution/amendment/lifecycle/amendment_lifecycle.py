from dataclasses import dataclass

from .amendment_state import AmendmentState


@dataclass(frozen=True)
class AmendmentLifecycle:

    proposal_id: str
    state: AmendmentState