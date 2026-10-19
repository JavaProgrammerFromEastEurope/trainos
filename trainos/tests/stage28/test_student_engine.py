from kernel.education.students.student import Student
from kernel.education.students.student_engine import StudentEngine
from kernel.education.students.student_status import StudentStatus


def test_student_engine():

    engine = StudentEngine()
    student = Student(
        student_id="S1",
        resident_id="R1",
        status=StudentStatus.ENROLLED,
    )
    studying = engine.begin(student)
    assert studying.status == StudentStatus.STUDYING
    graduated = engine.graduate(studying)
    assert graduated.status == StudentStatus.GRADUATED
