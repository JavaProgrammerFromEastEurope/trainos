from kernel.education.students.student_policy import StudentPolicy


def test_student_policy():

    policy = StudentPolicy(
        allow_graduation	= True,
        allow_dropout			= True,
    )

    assert policy.allow_graduation is True
    assert policy.allow_dropout is True
