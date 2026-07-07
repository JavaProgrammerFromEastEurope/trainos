from decimal import Decimal

from kernel.logistics.storage.storage_engine import StorageEngine
from kernel.logistics.storage.storage_record import StorageRecord
from kernel.logistics.storage.storage_status import StorageStatus


def test_storage_engine():

    engine = StorageEngine()

    record = StorageRecord(
        storage_id="ST1",
        warehouse_id="WH1",
        resource_id="water",
        quantity=Decimal("100"),
        status=StorageStatus.AVAILABLE,
    )

    result = engine.update(record)
    assert result is record
