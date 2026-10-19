from dataclasses import dataclass

from kernel.education.students.student_status import StudentStatus


@dataclass(frozen=True, slots=True)
class StudentSnapshot:

    student_id: str
    status: StudentStatus