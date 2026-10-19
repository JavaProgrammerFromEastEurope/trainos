from kernel.institution.authority.authority_level import AuthorityLevel
from kernel.institution.authority.constitutional_authority import ConstitutionalAuthority


def test_constitutional_authority_assignment():

    authority = ConstitutionalAuthority(
        institution_id="CC-001",
        level=AuthorityLevel.CONSTITUTIONAL,
    )

    assert authority.level is AuthorityLevel.CONSTITUTIONAL
    assert authority.institution_id == "CC-001"