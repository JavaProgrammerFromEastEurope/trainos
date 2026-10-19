from .composite_node import (
    CompositeNode,
)

from .node_status import (
    NodeStatus,
)


class SelectorNode(CompositeNode):

    def tick(self) -> NodeStatus:
        for child in self.children:
            result = child.tick()
            if result == NodeStatus.SUCCESS:
                return NodeStatus.SUCCESS
        return NodeStatus.FAILURE
