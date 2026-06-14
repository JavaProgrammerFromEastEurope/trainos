from __future__ import annotations

from .hierarchy_node import (
    HierarchyNode,
)


class HierarchyTree:

    def __init__(self):
        self._nodes: dict = {}

    def add(
        self,
        node: HierarchyNode,
    ) -> None:
        self._nodes[node.entity_id] = node

    def get(
        self,
        entity_id,
    ):
        return self._nodes.get(
            entity_id,
        )
