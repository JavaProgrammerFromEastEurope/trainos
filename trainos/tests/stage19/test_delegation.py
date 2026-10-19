from kernel.institution.delegation.delegation_registry import DelegationRegistry
from kernel.institution.delegation.delegation_scope import DelegationScope
from kernel.institution.delegation.institutional_delegation import (
    InstitutionalDelegation,
)


def test_register_delegation():

    registry = DelegationRegistry()

    delegation = InstitutionalDelegation(
        from_institution="CC-001",
        to_institution="EO-001",
        scope=DelegationScope.PERMANENT,
    )

    registry.register(delegation)

    assert (
        registry.get(
            "CC-001",
            "EO-001",
        )
        == delegation
    )
