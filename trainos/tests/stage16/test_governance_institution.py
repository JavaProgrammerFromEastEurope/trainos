from trainos.kernel.governance.institution.governance_institution import GovernanceInstitution
from trainos.kernel.governance.institution.institution_type import InstitutionType
from trainos.kernel.governance.authority import GovernanceAuthority
from trainos.kernel.governance.authority_level import AuthorityLevel


def test_governance_institution():
    institution = GovernanceInstitution(
        name="Constitutional Council",
        description="Top governance body",
        type=InstitutionType.LEGISLATIVE,
        authority=GovernanceAuthority(
            name="Council Authority",
            level=AuthorityLevel.CONSTITUTIONAL
        )
    )

    assert institution.type == InstitutionType.LEGISLATIVE