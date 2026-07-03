from dataclasses import dataclass


@dataclass(frozen=True)
class AuditPolicy:

    immutable_log: 				bool
    chronological_order: 	bool