from dataclasses import dataclass


@dataclass(frozen=True)
class AuditPolicy:

    immutable_log: 				bool
    require_reason: 			bool
    strict_actor_tracking: bool