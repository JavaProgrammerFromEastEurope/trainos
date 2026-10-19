from dataclasses import dataclass


@dataclass(frozen=True)
class AuditEvent:

    event_id: 	str
    actor_id: 	str
    action: 		str
    target_id: 	str
    reason: 		str | None