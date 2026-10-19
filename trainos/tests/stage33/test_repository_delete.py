from dataclasses import dataclass

from kernel.persistence.repositories.memory_repository import MemoryRepository


@dataclass
class Entity:
    object_id: str


def test_repository_delete():

    repository = MemoryRepository()
    entity = Entity(object_id="DELETE-1")
    repository.save(entity)
    deleted = repository.delete("DELETE-1")

    assert deleted.object_id == "DELETE-1"
    assert repository.get("DELETE-1") is None
