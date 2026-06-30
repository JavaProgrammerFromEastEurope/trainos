from trainos.kernel.identity.principles.reflection.reflection_status import (
    ReflectionStatus,
)


def test_reflection_status():
    status = ReflectionStatus.VALID

    assert status == ReflectionStatus.VALID
