from kernel.governance.definitions.governance_category import GovernanceCategory
from kernel.governance.definitions.governance_definition import GovernanceDefinition
from kernel.governance.definitions.governance_type import GovernanceType


def test_governance_definition():

    definition = GovernanceDefinition(
        governance_id="executive",
        name="Executive Authority",
        governance_type=GovernanceType.EXECUTIVE,
        category=GovernanceCategory.CIVIL,
    )

    assert definition.governance_id == "executive"
    assert definition.name == "Executive Authority"
    assert definition.governance_type == GovernanceType.EXECUTIVE
    assert definition.category == GovernanceCategory.CIVIL
