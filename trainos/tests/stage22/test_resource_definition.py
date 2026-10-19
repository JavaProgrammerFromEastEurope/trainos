from kernel.resources.definitions.resource_definition import ResourceDefinition
from kernel.resources.definitions.resource_type import ResourceType
from kernel.resources.definitions.resource_category import ResourceCategory
from kernel.resources.definitions.resource_unit import ResourceUnit


def test_resource_definition():

    unit = ResourceUnit(
        unit_id="liter",
        name="Liter",
        symbol="L",
    )

    definition = ResourceDefinition(
        resource_id="water",
        name="Water",
        resource_type=ResourceType.WATER,
        category=ResourceCategory.LIQUID,
        base_unit=unit,
        is_renewable=True,
    )

    assert definition.resource_id == "water"
    assert definition.name == "Water"
    assert definition.resource_type == ResourceType.WATER
    assert definition.category == ResourceCategory.LIQUID
    assert definition.base_unit == unit
    assert definition.is_renewable is True