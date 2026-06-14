from __future__ import annotations

from trainos.kernel.world.entities.entity import (
    Entity,
)


class SpatialIndex:

    def __init__(self):
        self._entities: list[Entity] = []

    def add(
        self,
        entity: Entity,
    ) -> None:
        self._entities.append(
            entity,
        )

    def remove(
        self,
        entity: Entity,
    ) -> None:
        if entity in self._entities:
            self._entities.remove(
                entity,
            )

    def entities(
        self,
    ) -> tuple[Entity, ...]:
        return tuple(
            self._entities,
        )
