from dataclasses import dataclass

from kernel.persistence.repositories.memory_repository import MemoryRepository


@dataclass
class Entity:
    object_id: str


def test_memory_repository():

    repository = MemoryRepository()
    entity = Entity(object_id="R1")
    repository.save(entity)
    result = repository.get("R1")
    assert result.object_id == "R1"
