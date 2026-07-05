from kernel.economy.audit.economic_audit_entry import EconomicAuditEntry
from kernel.economy.audit.economic_audit_registry import EconomicAuditRegistry


def test_economic_audit():

    registry = EconomicAuditRegistry()

    entry = EconomicAuditEntry(
        entry_id="AUD-1",
        actor_id="Government",
        action="collect_tax",
        reason="Monthly collection",
    )

    registry.register(entry)

    assert len(registry.entries()) == 1