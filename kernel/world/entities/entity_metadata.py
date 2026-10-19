from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class EntityMetadata:

    name: str
    description: str = ""

    tags: set[str] = field(
        default_factory=set,
    )
    created_tick: int = 0

    def add_tag(
        self,
        tag: str,
    ) -> None:
        self.tags.add(tag)

    def remove_tag(
        self,
        tag: str,
    ) -> None:
        self.tags.discard(tag)

    def has_tag(
        self,
        tag: str,
    ) -> bool:
        return tag in self.tags
