from kernel.resources.definitions.resource_category import ResourceCategory
from kernel.resources.definitions.resource_definition import ResourceDefinition
from kernel.resources.definitions.resource_type import ResourceType
from kernel.resources.definitions.resource_unit import ResourceUnit

from kernel.resources.inventory.resource_record import ResourceRecord
from kernel.resources.inventory.resource_registry import ResourceRegistry


def test_resource_registry():

    registry = ResourceRegistry()

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

    record = ResourceRecord(
        resource_id="water",
        definition=definition,
    )

    registry.register(record)

    assert registry.exists("water") is True

    loaded = registry.get("water")

    assert loaded is record
    assert loaded.resource_id == "water"
    assert loaded.definition == definition