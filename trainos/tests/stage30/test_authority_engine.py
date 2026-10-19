from kernel.governance.authorities.authority import Authority
from kernel.governance.authorities.authority_engine import AuthorityEngine
from kernel.governance.authorities.authority_status import AuthorityStatus


def test_authority_engine():

    engine = AuthorityEngine()

    authority = Authority(
        authority_id="A1",
        resident_id="R1",
        status=AuthorityStatus.ACTIVE,
    )

    suspended = engine.suspend(authority)
    assert suspended.status == AuthorityStatus.SUSPENDED

    activated = engine.activate(suspended)
    assert activated.status == AuthorityStatus.ACTIVE
