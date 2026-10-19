from .memory_repository import MemoryRepository


class RepositoryEngine:

    def __init__(self):
        self.repository = MemoryRepository()

    def save(self, obj):
        return self.repository.save(obj)

    def get(self, object_id):
        return self.repository.get(object_id)

    def delete(self, object_id):
        return self.repository.delete(object_id)
