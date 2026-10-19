from dataclasses import dataclass

from kernel.persistence.engine.persistence_engine import (
    PersistenceEngine,
)


@dataclass
class Entity:

    object_id: 	str
    name: 			str


def test_persistence_engine():

    engine = PersistenceEngine()
    entity = Entity(object_id="P1", name="Resident")

    saved = engine.save(entity)
    assert saved.success is True

    loaded = engine.load("P1")
    assert loaded.success is True
    assert loaded.data.name == "Resident"
