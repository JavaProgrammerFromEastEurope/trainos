from dataclasses import dataclass

from .storage_status import StorageStatus


@dataclass(frozen=True, slots=True)
class Storage:

    storage_id: str
    status: StorageStatus