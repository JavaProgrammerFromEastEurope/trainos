from abc import ABC, abstractmethod


class Repository(ABC):

    @abstractmethod
    def save(self, obj):
        pass

    @abstractmethod
    def get(self, object_id: str):
        pass

    @abstractmethod
    def delete(self, object_id: str):
        pass
