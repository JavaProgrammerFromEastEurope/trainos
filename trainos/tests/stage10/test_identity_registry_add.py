from kernel.civilization.identity.identity import Identity
from kernel.civilization.identity.identity_registry import IdentityRegistry
from kernel.civilization.identity.identity_type import IdentityType


def test_identity_registry_add():

    registry = IdentityRegistry()

    identity = Identity(
        type=IdentityType.SURVIVOR,
    )

    registry.add(identity)

    assert identity in registry.identities()