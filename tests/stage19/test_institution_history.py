from kernel.institution.history.institution_history_entry import InstitutionHistoryEntry
from kernel.institution.history.institution_history_registry import InstitutionHistoryRegistry


def test_register_history_entry():

    registry = InstitutionHistoryRegistry()

    entry = InstitutionHistoryEntry(
        institution_id="EO-001",
        version="1.0",
        description="Institution created",
    )

    registry.register(entry)
    history = registry.history("EO-001")

    assert len(history) == 1
    assert history[0] == entry