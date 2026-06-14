from trainos.kernel.world.relations.relation import (
    Relation,
)

from trainos.kernel.world.relations.relation_graph import (
    RelationGraph,
)

from trainos.kernel.world.relations.relation_type import (
    RelationType,
)


def test_relations():

    graph = RelationGraph()

    relation = Relation(
        source=1,
        target=2,
        type=RelationType.LINK,
    )

    graph.add(relation)

    assert len(graph.relations()) == 1

    assert graph.relations()[0] is relation

    graph.remove(relation)

    assert len(graph.relations()) == 0
