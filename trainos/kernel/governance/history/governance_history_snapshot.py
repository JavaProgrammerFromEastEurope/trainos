from dataclasses import dataclass

from kernel.governance.decisions.decision_status import (
    DecisionStatus,
)


@dataclass(frozen=True, slots=True)
class GovernanceHistorySnapshot:

    snapshot_id: str
    decision_id: str
    status: DecisionStatus