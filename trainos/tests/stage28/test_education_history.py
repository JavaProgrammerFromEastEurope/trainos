from kernel.education.history.education_history_engine import EducationHistoryEngine
from kernel.education.history.education_history_entry import EducationHistoryEntry
from kernel.education.history.education_history_snapshot import EducationHistorySnapshot
from kernel.education.students.student_status import StudentStatus


def test_education_history():

    engine 		= EducationHistoryEngine()
    snapshot 	= EducationHistorySnapshot(
        snapshot_id="HS1",
        student_id="S1",
        status=StudentStatus.STUDYING,
    )
    entry = EducationHistoryEntry(
        entry_id="HE1",
        timestamp="2026-01-01T00:00:00Z",
        snapshot=snapshot,
    )
    result = engine.record(entry)

    assert result is entry
