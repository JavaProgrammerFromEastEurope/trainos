from .decorator_node import (
    DecoratorNode,
)

from .node_status import (
    NodeStatus,
)


class InverterNode(DecoratorNode):

    def tick(
        self,
    ) -> NodeStatus:
        result = self.child.tick()
        if result == NodeStatus.SUCCESS:
            return NodeStatus.FAILURE
        if result == NodeStatus.FAILURE:
            return NodeStatus.SUCCESS
        return result
