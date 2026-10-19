from kernel.constitution.constitution_registry import ConstitutionRegistry
from kernel.constitution.constitutional_rule import ConstitutionalRule
from kernel.constitution.rule_type import RuleType


def test_constitution_registry():

    registry = ConstitutionRegistry()

    registry.register(
        ConstitutionalRule(
            name="Identity",
            description="Core identity rule",
            type=RuleType.IMMUTABLE,
        )
    )

    assert len(registry.rules()) == 1