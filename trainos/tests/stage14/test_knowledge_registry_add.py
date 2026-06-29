from trainos.kernel.intelligence.knowledge.knowledge_node import KnowledgeNode
from trainos.kernel.intelligence.knowledge.knowledge_registry import KnowledgeRegistry
from trainos.kernel.intelligence.knowledge.knowledge_type import KnowledgeType


def test_knowledge_registry_add():

    registry = KnowledgeRegistry()
    node = KnowledgeNode(
        type=KnowledgeType.FACT,
        content="water reserve stable",
    )
    registry.add(node)
    assert registry.nodes() == (node,)
