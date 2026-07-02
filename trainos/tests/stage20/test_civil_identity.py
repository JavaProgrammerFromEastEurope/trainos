from kernel.society.identity.civil_identity import CivilIdentity
from kernel.society.identity.identity_role import IdentityRole


def test_create_civil_identity():

    identity = CivilIdentity(
        entity_id="A-104",
        role=IdentityRole.CITIZEN,
    )

    assert identity.entity_id == "A-104"
    assert identity.role is IdentityRole.CITIZEN
