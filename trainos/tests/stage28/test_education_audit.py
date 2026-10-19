from kernel.education.audit.education_audit_engine import EducationAuditEngine
from kernel.education.audit.education_audit_entry import EducationAuditEntry


def test_education_audit():

    engine = EducationAuditEngine()
    entry = EducationAuditEntry(
        audit_id="AUD1",
        actor_id="teacher",
        student_id="S1",
        action="graduate_student",
    )
    result = engine.record(entry)

    assert result is entry