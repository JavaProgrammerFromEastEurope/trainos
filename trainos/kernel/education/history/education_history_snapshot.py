from dataclasses import dataclass

from kernel.education.students.student_status import StudentStatus


@dataclass(frozen=True, slots=True)
class EducationHistorySnapshot:

    snapshot_id: 	str
    student_id: 	str
    status: StudentStatus