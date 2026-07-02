from trainos.kernel.constitution.constitution_registry import ConstitutionRegistry
from trainos.kernel.constitution.constitutional_rule import ConstitutionalRule
from trainos.kernel.constitution.rule_type import RuleType


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