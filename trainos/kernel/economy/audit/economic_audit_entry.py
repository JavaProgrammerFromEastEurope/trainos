from dataclasses import dataclass


@dataclass(frozen=True)
class EconomicAuditEntry:

    entry_id: str
    actor_id: str
    action: 	str
    reason: 	str