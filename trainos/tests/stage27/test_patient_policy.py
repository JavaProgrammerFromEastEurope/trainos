from kernel.healthcare.patients.patient_policy import PatientPolicy


def test_patient_policy():

    policy = PatientPolicy(
        allow_treatment=True,
        allow_discharge=True,
    )

    assert policy.allow_treatment is True
    assert policy.allow_discharge is True