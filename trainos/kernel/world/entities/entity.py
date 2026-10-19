from __future__ import annotations

from dataclasses import dataclass

from .entity_id import (
    EntityId,
)

from .entity_metadata import (
    EntityMetadata,
)

from .entity_type import (
    EntityType,
)


@dataclass
class Entity:

    id: 			EntityId
    type: 		EntityType
    metadata: EntityMetadata

    def rename(
        self,
        name: str,
    ) -> None:
        self.metadata.name = name

    def add_tag(
        self,
        tag: str,
    ) -> None:
        self.metadata.add_tag(tag)

    def remove_tag(
        self,
        tag: str,
    ) -> None:
        self.metadata.remove_tag(tag)

    def has_tag(
        self,
        tag: str,
    ) -> bool:
        return self.metadata.has_tag(tag)
