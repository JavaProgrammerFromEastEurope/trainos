from trainos.kernel.evolution.identity.identity_registry import IdentityRegistry
from trainos.kernel.evolution.identity.identity_snapshot import IdentitySnapshot


def test_identity_registry_register():

    registry = IdentityRegistry()

    snapshot = IdentitySnapshot(
        generation=1,
        description="founding generation",
    )

    registry.register(snapshot)

    assert registry.snapshots() == (snapshot,)