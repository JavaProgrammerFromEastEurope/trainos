from __future__ import annotations

from .entity import (
    Entity,
)

from .entity_id import (
    EntityId,
)


class EntityRegistry:

    def __init__(
        self,
    ) -> None:
        self._entities: dict[
            EntityId,
            Entity,
        ] = {}

    def register(
        self,
        entity: Entity,
    ) -> None:
        self._entities[entity.id] = entity

    def get(
        self,
        entity_id: EntityId,
    ) -> Entity | None:
        return self._entities.get(
            entity_id,
        )

    def remove(
        self,
        entity_id: EntityId,
    ) -> None:
        self._entities.pop(
            entity_id,
            None,
        )

    def exists(
        self,
        entity_id: EntityId,
    ) -> bool:
        return entity_id in self._entities

    def all(
        self,
    ) -> tuple[Entity, ...]:
        return tuple(
            self._entities.values(),
        )

    def count(
        self,
    ) -> int:
        return len(
            self._entities,
        )

    def clear(
        self,
    ) -> None:
        self._entities.clear()
