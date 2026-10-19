from __future__ import annotations

from .htn_node import (
    HTNNode,
)


class HTNGraph:

    def __init__(
        self,
    ) -> None:
        self._nodes: list[HTNNode] = []

    def add(
        self,
        node: HTNNode,
    ) -> None:
        self._nodes.append(node)

    def nodes(
        self,
    ) -> tuple[HTNNode, ...]:
        return tuple(self._nodes)
