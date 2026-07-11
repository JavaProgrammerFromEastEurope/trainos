from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class EducationAuditEntry:

    audit_id: 		str
    actor_id: 		str
    student_id: 	str
    action: 			str