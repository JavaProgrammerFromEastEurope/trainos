from .student import Student
from .student_status import StudentStatus


class StudentEngine:

    def begin(
        self,
        student: Student,
    ) -> Student:
        return Student(
            student_id=student.student_id,
            resident_id=student.resident_id,
            status=StudentStatus.STUDYING,
        )

    def graduate(
        self,
        student: Student,
    ) -> Student:
        return Student(
            student_id=student.student_id,
            resident_id=student.resident_id,
            status=StudentStatus.GRADUATED,
        )
