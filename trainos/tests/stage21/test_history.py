from decimal import Decimal

from kernel.economy.history.economic_snapshot import EconomicSnapshot
from kernel.economy.history.economic_history_entry import EconomicHistoryEntry
from kernel.economy.history.economic_history_registry import EconomicHistoryRegistry


def test_history():

    snapshot = EconomicSnapshot(
        snapshot_id="S1",
        treasury_assets=Decimal("1000"),
        planned_budget=Decimal("800"),
        collected_tax=Decimal("120"),
    )

    entry = EconomicHistoryEntry(
        entry_id="H1",
        timestamp="2027",
        snapshot=snapshot,
    )

    registry = EconomicHistoryRegistry()
    registry.register(entry)

    assert registry.entries()[0].snapshot.snapshot_id == "S1"
