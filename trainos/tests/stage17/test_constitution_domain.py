from kernel.constitution.domain.constitutional_domain import ConstitutionalDomain
from kernel.constitution.domain.domain_type import DomainType


def test_constitution_domain():

    domain = ConstitutionalDomain(
        rule_name="Voting",
        domain=DomainType.GOVERNANCE,
    )

    assert domain.domain == DomainType.GOVERNANCE