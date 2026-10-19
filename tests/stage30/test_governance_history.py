from kernel.governance.decisions.decision_status import DecisionStatus
from kernel.governance.history.governance_history_engine import GovernanceHistoryEngine
from kernel.governance.history.governance_history_entry import GovernanceHistoryEntry
from kernel.governance.history.governance_history_snapshot import (
    GovernanceHistorySnapshot,
)


def test_governance_history():

    engine = GovernanceHistoryEngine()
    snapshot = GovernanceHistorySnapshot(
        snapshot_id="HS1",
        decision_id="D1",
        status=DecisionStatus.APPROVED,
    )
    entry = GovernanceHistoryEntry(
        entry_id="HE1",
        timestamp="2026-01-01T00:00:00Z",
        snapshot=snapshot,
    )

    result = engine.record(entry)
    assert result is entry
