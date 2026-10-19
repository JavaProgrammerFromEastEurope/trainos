from dataclasses import dataclass

from .governance_history_snapshot import (
    GovernanceHistorySnapshot,
)


@dataclass(frozen=True, slots=True)
class GovernanceHistoryEntry:

    entry_id: 	str
    timestamp: 	str
    snapshot: GovernanceHistorySnapshot