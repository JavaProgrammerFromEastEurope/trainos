from __future__ import annotations

from .bt_node import (
    BTNode,
)


class CompositeNode(
    BTNode,
):

    def __init__(
        self,
    ) -> None:
        self.children: list[BTNode] = []

    def add_child(
        self,
        child: BTNode,
    ) -> None:
        self.children.append(
            child,
        )
