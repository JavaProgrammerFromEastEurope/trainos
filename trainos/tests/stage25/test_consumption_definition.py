from kernel.consumption.definitions.consumption_category import ConsumptionCategory
from kernel.consumption.definitions.consumption_definition import ConsumptionDefinition
from kernel.consumption.definitions.consumption_type import ConsumptionType


def test_consumption_definition():

    definition = ConsumptionDefinition(
        consumption_id="hospital_water",
        name="Hospital Water",
        consumption_type=ConsumptionType.WATER,
        category=ConsumptionCategory.ESSENTIAL,
    )

    assert definition.consumption_id == "hospital_water"
    assert definition.name == "Hospital Water"
    assert definition.consumption_type == ConsumptionType.WATER
    assert definition.category == ConsumptionCategory.ESSENTIAL