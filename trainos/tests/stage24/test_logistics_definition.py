from kernel.logistics.definitions.logistics_category import LogisticsCategory
from kernel.logistics.definitions.logistics_definition import LogisticsDefinition
from kernel.logistics.definitions.logistics_type import LogisticsType


def test_logistics_definition():

    definition = LogisticsDefinition(
        logistics_id="water_supply",
        name="Water Supply",
        logistics_type=LogisticsType.SUPPLY,
        category=LogisticsCategory.AUTOMATED,
    )

    assert definition.logistics_id == "water_supply"
    assert definition.name == "Water Supply"
    assert definition.logistics_type == LogisticsType.SUPPLY
    assert definition.category == LogisticsCategory.AUTOMATED