from dataclasses import dataclass

from trainos.kernel.world.entities.entity_id import (
    EntityId,
)


@dataclass
class Collision:
    entity_a: EntityId
    entity_b: EntityId
