from dataclasses import asdict


class Serializer:

    def serialize(
        self,
        obj: object,
    ) -> dict:
        return asdict(obj)
