from dataclasses import dataclass

from kernel.persistence.serialization.serializer import Serializer


@dataclass(frozen=True, slots=True)
class Entity:

    object_id: str
    value: int


def test_serializer():
    entity = Entity(
        object_id="E1",
        value=100,
    )
    result = Serializer().serialize(entity)

    assert result["object_id"] == "E1"
    assert result["value"] == 100
