from .bt_node import (
    BTNode,
)


class DecoratorNode(BTNode):

    def __init__(
        self,
        child: BTNode,
    ) -> None:
        self.child = child
