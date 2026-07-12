from dataclasses import dataclass

from kernel.persistence.storage.storage_status import StorageStatus


@dataclass(frozen=True, slots=True)
class StorageSnapshot:

    storage_id: str
    status: StorageStatus
