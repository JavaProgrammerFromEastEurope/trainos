from dataclasses import dataclass

from kernel.world.entities.entity_id import (
    EntityId,
)


@dataclass
class HierarchyNode:

    entity_id: EntityId
    parent: EntityId | None
