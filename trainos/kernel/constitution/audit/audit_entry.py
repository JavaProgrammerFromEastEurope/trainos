from dataclasses import dataclass


@dataclass(frozen=True)
class ConstitutionalAuditEntry:

    version: 			str
    proposal_id: 	str
    authority: 		str
    reason: 			str