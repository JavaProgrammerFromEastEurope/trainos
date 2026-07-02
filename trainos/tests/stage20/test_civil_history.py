from kernel.society.history.civil_history_entry import CivilHistoryEntry
from kernel.society.history.civil_history_registry import CivilHistoryRegistry


def test_register_history_entry():

    registry = CivilHistoryRegistry()

    entry = CivilHistoryEntry(
        entity_id="A-104",
        version="1.0",
        description="Citizen registered",
    )

    registry.register(entry)
    history = registry.history("A-104")

    assert len(history) == 1
    assert history[0] == entry
