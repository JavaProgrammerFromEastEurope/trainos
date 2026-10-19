from dataclasses import dataclass

from kernel.persistence.serialization.deserializer import Deserializer


@dataclass(frozen=True, slots=True)
class Entity:

    object_id: str
    value: int


def test_deserializer():

    data = {"object_id": "E2", "value": 200}
    entity = Deserializer().deserialize(data, Entity)

    assert entity.object_id == "E2"
    assert entity.value == 200
