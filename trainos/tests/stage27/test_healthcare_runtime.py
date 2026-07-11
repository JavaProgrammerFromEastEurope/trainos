from kernel.healthcare.runtime.healthcare_runtime import HealthcareRuntime


def test_healthcare_runtime():

    runtime = HealthcareRuntime()
    runtime.initialize()
    runtime.update()
    runtime.shutdown()

    assert runtime.context is not None