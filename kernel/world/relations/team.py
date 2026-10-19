from dataclasses import dataclass

from kernel.world.entities.entity_id import (
    EntityId,
)


@dataclass
class Team:

    name: str
    members: list[EntityId]
