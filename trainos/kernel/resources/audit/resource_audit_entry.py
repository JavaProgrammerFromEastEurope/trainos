from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class ResourceAuditEntry:

    audit_id: str
    actor_id: str
    action: str
    resource_id: str
    reason: str | None = None