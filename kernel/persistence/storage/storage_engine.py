from .storage import Storage
from .storage_status import StorageStatus


class StorageEngine:

    def initialize(
        self,
        storage: Storage,
    ) -> Storage:
        return Storage(
            storage_id=storage.storage_id,
            status=StorageStatus.RUNNING,
        )

    def pause(
        self,
        storage: Storage,
    ) -> Storage:
        return Storage(
            storage_id=storage.storage_id,
            status=StorageStatus.PAUSED,
        )

    def stop(
        self,
        storage: Storage,
    ) -> Storage:
        return Storage(
            storage_id=storage.storage_id,
            status=StorageStatus.STOPPED,
        )
