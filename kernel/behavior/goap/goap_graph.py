from __future__ import annotations

from .goap_node import (
    GOAPNode,
)


class GOAPGraph:

    def __init__(
        self,
    ) -> None:
        self._nodes: list[GOAPNode] = []

    def add(
        self,
        node: GOAPNode,
    ) -> None:
        self._nodes.append(node)

    def nodes(
        self,
    ) -> tuple[GOAPNode, ...]:
        return tuple(self._nodes)
