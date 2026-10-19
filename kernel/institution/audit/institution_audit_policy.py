from dataclasses import dataclass


@dataclass(frozen=True)
class InstitutionAuditPolicy:

    immutable_entries: 	bool
    require_reason: 		bool