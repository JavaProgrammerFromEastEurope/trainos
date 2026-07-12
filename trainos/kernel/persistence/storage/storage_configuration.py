from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class StorageConfiguration:

    storage_name: str
    backend: 			str