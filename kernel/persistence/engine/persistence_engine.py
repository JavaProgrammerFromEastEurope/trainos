from kernel.persistence.serialization.serialization_engine import SerializationEngine

from kernel.persistence.repositories.repository_engine import RepositoryEngine
from .persistence_result import PersistenceResult


class PersistenceEngine:

    def __init__(self):
        self.serializer = SerializationEngine()
        self.repository = RepositoryEngine()

    def save(self, obj) -> PersistenceResult:
        data = self.serializer.encode(obj)
        stored = self.repository.save(obj)
        return PersistenceResult(
            success=True,
            data=stored,
        )

    def load(self, object_id) -> PersistenceResult:
        obj = self.repository.get(object_id)
        return PersistenceResult(
            success=obj is not None,
            data=obj,
        )

    def delete(self, object_id) -> PersistenceResult:
        result = self.repository.delete(object_id)
        return PersistenceResult(
            success=result is not None,
            data=result,
        )
