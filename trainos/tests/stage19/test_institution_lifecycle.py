from kernel.institution.lifecycle.institution_lifecycle import InstitutionLifecycle
from kernel.institution.lifecycle.institution_state import InstitutionState


def test_lifecycle_creation():

    lifecycle = InstitutionLifecycle(
        institution_id="EO-001",
        state=InstitutionState.ACTIVE,
    )

    assert lifecycle.institution_id == "EO-001"
    assert lifecycle.state is InstitutionState.ACTIVE