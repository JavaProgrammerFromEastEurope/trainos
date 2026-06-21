from trainos.kernel.communication.memory.knowledge_graph import KnowledgeGraph
from trainos.kernel.communication.memory.knowledge_node import KnowledgeNode


def test_knowledge_graph_add_multiple():

    graph = KnowledgeGraph()

    node_1 = KnowledgeNode(name="food")
    node_2 = KnowledgeNode(name="water")

    graph.add(node_1)
    graph.add(node_2)

    assert graph.nodes() == (node_1, node_2)
