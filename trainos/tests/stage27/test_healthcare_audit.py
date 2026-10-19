from kernel.healthcare.audit.healthcare_audit_engine import HealthcareAuditEngine
from kernel.healthcare.audit.healthcare_audit_entry import HealthcareAuditEntry


def test_healthcare_audit():

    engine = HealthcareAuditEngine()
    entry = HealthcareAuditEntry(
        audit_id="AUD1",
        actor_id="doctor",
        patient_id="P1",
        action="start_treatment",
    )

    result = engine.record(entry)
    assert result is entry