from kernel.institution.hierarchy.hierarchy_relation import HierarchyRelation
from kernel.institution.hierarchy.hierarchy_registry import HierarchyRegistry


def test_register_hierarchy_relation():

    registry = HierarchyRegistry()

    relation = HierarchyRelation(
        parent_id="CC-001",
        child_id="EO-001",
    )

    registry.register(relation)

    relations = registry.relations()

    assert len(relations) == 1

    assert relations[0] == relation