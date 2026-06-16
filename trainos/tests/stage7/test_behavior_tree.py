from trainos.kernel.behavior.tree.behavior_tree import (
    BehaviorTree,
)

from trainos.kernel.behavior.tree.bt_node import BTNode
from trainos.kernel.behavior.tree.node_status import NodeStatus


class DummyNode(BTNode):

    def tick(
        self,
    ) -> NodeStatus:
        return NodeStatus.SUCCESS


def test_behavior_tree():

    tree = BehaviorTree(DummyNode())
    result = tree.tick()
    assert result == NodeStatus.SUCCESS
