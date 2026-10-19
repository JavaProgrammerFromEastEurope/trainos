from .storage_record import StorageRecord


class StorageEngine:

    def update(
        self,
        record: StorageRecord,
    ) -> StorageRecord:
        return record
