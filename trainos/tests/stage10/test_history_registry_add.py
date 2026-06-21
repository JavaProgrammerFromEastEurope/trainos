from trainos.kernel.civilization.history.historical_record import HistoricalRecord
from trainos.kernel.civilization.history.history_registry import HistoryRegistry


def test_history_registry_add():

    registry = HistoryRegistry()

    record = HistoricalRecord(
        description="system stabilized after crisis",
    )

    registry.add(record)

    assert registry.records() == (record,)
