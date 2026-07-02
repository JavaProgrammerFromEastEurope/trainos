from trainos.kernel.constitution.hierarchy.constitutional_hierarchy import ConstitutionalHierarchy
from trainos.kernel.constitution.hierarchy.hierarchy_level import HierarchyLevel


def test_constitution_hierarchy():

    hierarchy = ConstitutionalHierarchy(
        rule_name="Identity",
        level=HierarchyLevel.FOUNDATIONAL,
    )

    assert hierarchy.level == HierarchyLevel.FOUNDATIONAL