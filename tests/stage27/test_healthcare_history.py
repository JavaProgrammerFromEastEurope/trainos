from kernel.healthcare.history.healthcare_history_engine import HealthcareHistoryEngine
from kernel.healthcare.history.healthcare_history_entry import HealthcareHistoryEntry
from kernel.healthcare.history.healthcare_history_snapshot import HealthcareHistorySnapshot
from kernel.healthcare.patients.patient_status import PatientStatus


def test_healthcare_history():

    engine = HealthcareHistoryEngine()
    snapshot = HealthcareHistorySnapshot(
        snapshot_id="S1",
        patient_id="P1",
        status=PatientStatus.IN_TREATMENT,
    )
    entry = HealthcareHistoryEntry(
        entry_id="E1",
        timestamp="2026-01-01T00:00:00Z",
        snapshot=snapshot,
    )

    result = engine.record(entry)
    assert result is entry