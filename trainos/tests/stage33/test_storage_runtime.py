from kernel.persistence.storage.storage import Storage

from kernel.persistence.storage.storage_status import StorageStatus
from kernel.persistence.storage.storage_engine import StorageEngine


def test_storage_runtime():

    storage = Storage(
        storage_id="ST1",
        status=StorageStatus.CREATED,
    )

    engine = StorageEngine()
    storage = engine.initialize(storage)

    assert storage.status == StorageStatus.RUNNING

    storage = engine.pause(storage)
    assert storage.status == StorageStatus.PAUSED

    storage = engine.stop(storage)
    assert storage.status == StorageStatus.STOPPED
