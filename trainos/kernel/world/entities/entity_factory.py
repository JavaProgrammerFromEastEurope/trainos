from __future__ import annotations

from uuid import uuid4

from .entity import (
    Entity,
)

from .entity_id import (
    EntityId,
)

from .entity_metadata import (
    EntityMetadata,
)

from .entity_type import (
    EntityType,
)


class EntityFactory:

    def create(
        self,
        entity_type: EntityType,
        name: str,
    ) -> Entity:
        return Entity(
            id=EntityId(
                str(uuid4()),
            ),
            type=entity_type,
            metadata=EntityMetadata(
                name=name,
            ),
        )

    def create_human(
        self,
        name: str,
    ) -> Entity:
        return self.create(
            EntityType.HUMAN,
            name,
        )

    def create_drone(
        self,
        name: str,
    ) -> Entity:
        return self.create(
            EntityType.DRONE,
            name,
        )

    def create_vehicle(
        self,
        name: str,
    ) -> Entity:
        return self.create(
            EntityType.VEHICLE,
            name,
        )
