from dataclasses import dataclass

from trainos.kernel.world.entities.entity_id import (
    EntityId,
)
from .relation_type import (
    RelationType,
)


@dataclass
class Relation:

    source: EntityId
    target: EntityId
    type: RelationType
