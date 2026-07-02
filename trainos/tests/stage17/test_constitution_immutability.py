from trainos.kernel.constitution.immutability.constitutional_immutability import (
    ConstitutionalImmutability,
)
from trainos.kernel.constitution.immutability.immutability_type import ImmutabilityType


def test_constitution_immutability():

    immutability = ConstitutionalImmutability(
        rule_name="Human dignity",
        type=ImmutabilityType.ABSOLUTE,
    )

    assert immutability.type == ImmutabilityType.ABSOLUTE
