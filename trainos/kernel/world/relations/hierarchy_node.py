from dataclasses import dataclass

from trainos.kernel.world.entities.entity_id import (
    EntityId,
)


@dataclass
class HierarchyNode:

    entity_id: EntityId
    parent: EntityId | None
