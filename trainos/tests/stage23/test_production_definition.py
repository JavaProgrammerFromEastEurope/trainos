from kernel.production.definitions.production_category import ProductionCategory
from kernel.production.definitions.production_definition import ProductionDefinition
from kernel.production.definitions.production_type import ProductionType


def test_production_definition():

    definition = ProductionDefinition(
        production_id="water_purification",
        name="Water Purification",
        production_type=ProductionType.WATER,
        category=ProductionCategory.CONTINUOUS,
    )

    assert definition.production_id == "water_purification"
    assert definition.name == "Water Purification"
    assert definition.production_type == ProductionType.WATER
    assert definition.category == ProductionCategory.CONTINUOUS