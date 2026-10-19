from __future__ import annotations

from .bt_node import (
    BTNode,
)

from .node_status import (
    NodeStatus,
)


class BehaviorTree:

    def __init__(
        self,
        root: BTNode,
    ) -> None:
        self.root = root

    def tick(
        self,
    ) -> NodeStatus:
        return self.root.tick()
