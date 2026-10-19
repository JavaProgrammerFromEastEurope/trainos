from __future__ import annotations

from .hierarchy_node import HierarchyNode


class HierarchyTree:

    def __init__(self) -> None:
        self._nodes: list[HierarchyNode] = []

    def add(self, node: HierarchyNode) -> None:
        self._nodes.append(node)

    def nodes(self) -> tuple[HierarchyNode, ...]:
        return tuple(self._nodes)
