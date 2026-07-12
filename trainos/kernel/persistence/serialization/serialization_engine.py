from .serializer import Serializer
from .deserializer import Deserializer


class SerializationEngine:

    def __init__(self):
        self.serializer 	= Serializer()
        self.deserializer = Deserializer()

    def encode(self, obj: object) -> dict:
        return self.serializer.serialize(obj)

    def decode(
        self,
        data: dict,
        target_type,
    ):
        return self.deserializer.deserialize(data, target_type)
