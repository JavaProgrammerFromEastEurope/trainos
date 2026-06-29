from trainos.kernel.intelligence.distributed.distributed_registry import (
    DistributedRegistry,
)
from trainos.kernel.intelligence.distributed.reasoning_node import ReasoningNode


def test_distributed_registry_register():

    registry = DistributedRegistry()
    node = ReasoningNode(
        identifier="engineering",
    )
    registry.register(node)
    assert registry.nodes() == (node,)
