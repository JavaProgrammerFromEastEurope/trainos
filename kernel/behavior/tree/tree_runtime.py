from __future__ import annotations

from .behavior_tree import (
    BehaviorTree,
)

from .node_status import (
    NodeStatus,
)


class TreeRuntime:

    def __init__(
        self,
        tree: BehaviorTree,
    ) -> None:
        self.tree = tree

    def tick(
        self,
    ) -> NodeStatus:
        return self.tree.tick()
