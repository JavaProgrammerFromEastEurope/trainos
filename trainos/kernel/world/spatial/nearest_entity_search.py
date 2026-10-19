from __future__ import annotations

from kernel.world.entities.entity import (
    Entity,
)


class NearestEntitySearch:

    def find(
        self,
        entities: list[Entity],
    ) -> Entity | None:
        if not entities:
            return None
        return entities[0]
