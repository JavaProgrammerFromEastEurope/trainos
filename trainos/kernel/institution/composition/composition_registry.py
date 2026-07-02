from __future__ import annotations

from .composition_relation import CompositionRelation


class CompositionRegistry:

    def __init__(self) -> None:
        self._relations: dict[str, tuple[CompositionRelation, ...]] = {}

    def register(self, relation: CompositionRelation) -> None:
        current = self._relations.get(relation.container_id, ())
        self._relations[relation.container_id] = current + (relation,)

    def components(
        self,
        container_id: str,
    ) -> tuple[CompositionRelation, ...]:
        return self._relations.get(container_id, ())
