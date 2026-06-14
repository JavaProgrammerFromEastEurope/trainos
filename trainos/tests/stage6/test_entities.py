from trainos.kernel.world.entities.entity import (
    Entity,
)

from trainos.kernel.world.entities.entity_id import (
    EntityId,
)

from trainos.kernel.world.entities.entity_metadata import (
    EntityMetadata,
)

from trainos.kernel.world.entities.entity_registry import (
    EntityRegistry,
)

from trainos.kernel.world.entities.entity_type import (
    EntityType,
)


def test_entities():

    registry = EntityRegistry()

    entity_id = EntityId(1)

    entity = Entity(
        id=entity_id,
        type=EntityType.DRONE,
        metadata=EntityMetadata(name="entity"),
    )

    registry.register(entity)

    assert registry.count() == 1

    assert registry.exists(entity_id) is True

    assert registry.get(entity_id) is entity

    entity.rename("drone")

    assert entity.metadata.name == "drone"

    entity.add_tag("flying")

    assert entity.has_tag("flying") is True

    entity.remove_tag("flying")

    assert entity.has_tag("flying") is False

    registry.remove(entity_id)

    assert registry.count() == 0
