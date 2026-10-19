from kernel.institution.composition.composition_relation import CompositionRelation
from kernel.institution.composition.composition_registry import CompositionRegistry


def test_register_composition():

    registry = CompositionRegistry()

    relation = CompositionRelation(
        container_id="EO-001",
        component_id="MD-001",
    )

    registry.register(relation)
    components = registry.components("EO-001")

    assert len(components) == 1
    assert components[0] == relation