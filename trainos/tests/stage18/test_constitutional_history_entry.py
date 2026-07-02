from trainos.kernel.constitution.history.history_entry import ConstitutionalHistoryEntry


def test_constitutional_history_entry():

    entry = ConstitutionalHistoryEntry(
        version="2.1",
        amendment_id="A-001",
    )

    assert entry.version == "2.1"