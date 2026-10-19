from kernel.security.definitions.security_category import SecurityCategory
from kernel.security.definitions.security_definition import SecurityDefinition
from kernel.security.definitions.security_type import SecurityType


def test_security_definition():

    definition = SecurityDefinition(
        security_id="internal_security",
        name="Internal Security",
        security_type=SecurityType.INTERNAL,
        category=SecurityCategory.PROTECTION,
    )

    assert definition.security_id == "internal_security"
    assert definition.name == "Internal Security"
    assert definition.security_type == SecurityType.INTERNAL
    assert definition.category == SecurityCategory.PROTECTION