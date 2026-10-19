from kernel.education.runtime.education_runtime import EducationRuntime


def test_education_runtime():

    runtime = EducationRuntime()
    runtime.initialize()
    runtime.update()
    runtime.shutdown()

    assert runtime.context is not None