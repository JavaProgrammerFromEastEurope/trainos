from trainos.kernel.intelligence.knowledge.knowledge_graph import KnowledgeGraph


def test_knowledge_graph_connect():

    graph = KnowledgeGraph()
    graph.connect("water", "food")

    assert graph.connections() == (("water", "food"),)
