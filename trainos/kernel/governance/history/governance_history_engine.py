from .governance_history_entry import (
    GovernanceHistoryEntry,
)


class GovernanceHistoryEngine:

    def record(
        self,
        entry: GovernanceHistoryEntry,
    ) -> GovernanceHistoryEntry:
        return entry
