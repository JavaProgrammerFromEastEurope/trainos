from dataclasses import dataclass

from .student_status import StudentStatus


@dataclass(frozen=True, slots=True)
class Student:

    student_id: str
    resident_id: str
    status: StudentStatus