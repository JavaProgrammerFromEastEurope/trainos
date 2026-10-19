from __future__ import annotations

from .hierarchy_relation import HierarchyRelation


class HierarchyRegistry:

    def __init__(self) -> None:
        self._relations: list[HierarchyRelation] = []

    def register(self, relation: HierarchyRelation) -> None:
        self._relations.append(relation)

    def relations(self) -> tuple[HierarchyRelation, ...]:
        return tuple(self._relations)
