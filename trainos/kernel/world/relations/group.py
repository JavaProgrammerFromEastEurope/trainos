from dataclasses import dataclass

from kernel.world.entities.entity_id import (
    EntityId,
)


@dataclass
class Group:

    name: 		str
    members: 	list[EntityId]
