from trainos.kernel.constitution.constitutional_rule import ConstitutionalRule
from trainos.kernel.constitution.rule_type import RuleType


def test_constitutional_rule_creation():

    rule = ConstitutionalRule(
        name="Human dignity",
        description="Foundational constitutional article",
        type=RuleType.IMMUTABLE,
    )

    assert rule.name == "Human dignity"
    assert rule.type == RuleType.IMMUTABLE