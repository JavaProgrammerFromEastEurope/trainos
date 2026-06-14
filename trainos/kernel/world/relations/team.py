from dataclasses import dataclass

from trainos.kernel.world.entities.entity_id import (
    EntityId,
)


@dataclass
class Team:

    name: str
    members: list[EntityId]
