from trainos.kernel.constitution.guardian.constitutional_guardian import ConstitutionalGuardian
from trainos.kernel.constitution.guardian.guardian_status import GuardianStatus


def test_constitution_guardian():

    guardian = ConstitutionalGuardian(
        name="Constitutional Guardian",
        status=GuardianStatus.ACTIVE,
    )

    assert guardian.status == GuardianStatus.ACTIVE