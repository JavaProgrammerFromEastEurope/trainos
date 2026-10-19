class MemoryRepository:

    def __init__(self):
        self.storage = {}

    def save(self, obj):
        self.storage[obj.object_id] = obj
        return obj

    def get(self, object_id: str):
        return self.storage.get(object_id)

    def delete(self, object_id: str):
        return self.storage.pop(object_id, None)
