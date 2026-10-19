from .composite_node import (
    CompositeNode,
)

from .node_status import (
    NodeStatus,
)


class SequenceNode(CompositeNode):

    def tick(
        self,
    ) -> NodeStatus:
        for child in self.children:
            result = child.tick()
            if result != NodeStatus.SUCCESS:
                return result
        return NodeStatus.SUCCESS
