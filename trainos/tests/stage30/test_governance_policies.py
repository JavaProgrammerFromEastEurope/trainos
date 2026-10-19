from kernel.governance.authorities.authority_policy import AuthorityPolicy
from kernel.governance.offices.governance_office_policy import GovernanceOfficePolicy
from kernel.governance.policies.policy_configuration import PolicyConfiguration
from kernel.governance.decisions.decision_policy import DecisionPolicy


def test_governance_policies():

    authority = AuthorityPolicy()
    decision = DecisionPolicy()
    office = GovernanceOfficePolicy()
    policy = PolicyConfiguration()

    assert authority.allow_decisions is True
    assert decision.allow_execution is True
    assert office.allow_operation is True
    assert policy.allow_activation is True
