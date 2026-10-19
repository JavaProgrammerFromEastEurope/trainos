from __future__ import annotations

from .node_status import (
    NodeStatus,
)


class BTNode:

    def tick(
        self,
    ) -> NodeStatus:
        return NodeStatus.SUCCESS
