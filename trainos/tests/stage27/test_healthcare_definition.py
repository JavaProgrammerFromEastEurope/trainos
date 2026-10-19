from kernel.healthcare.definitions.healthcare_category import HealthcareCategory
from kernel.healthcare.definitions.healthcare_definition import HealthcareDefinition
from kernel.healthcare.definitions.healthcare_type import HealthcareType


def test_healthcare_definition():

    definition = HealthcareDefinition(
        healthcare_id="general",
        name="General Healthcare",
        healthcare_type=HealthcareType.PHYSICAL,
        category=HealthcareCategory.PRIMARY,
    )

    assert definition.healthcare_id == "general"
    assert definition.name == "General Healthcare"
    assert definition.healthcare_type == HealthcareType.PHYSICAL
    assert definition.category == HealthcareCategory.PRIMARY