class Deserializer:

    def deserialize(
        self,
        data: dict,
        target_type,
    ):
        return target_type(**data)
