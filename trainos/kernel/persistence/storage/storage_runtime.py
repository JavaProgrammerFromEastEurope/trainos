from dataclasses import dataclass


@dataclass(slots=True)
class StorageRuntime:

    storage: object
