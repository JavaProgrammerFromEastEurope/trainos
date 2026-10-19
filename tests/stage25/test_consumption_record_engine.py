from decimal import Decimal

from kernel.consumption.records.consumption_record import ConsumptionRecord
from kernel.consumption.records.consumption_record_engine import ConsumptionRecordEngine
from kernel.consumption.records.consumption_record_status import ConsumptionRecordStatus


def test_consumption_record_engine():

    engine = ConsumptionRecordEngine()

    record = ConsumptionRecord(
        record_id="REC1",
        consumer_id="C1",
        resource_id="water",
        quantity=Decimal("50"),
        status=ConsumptionRecordStatus.RECORDED,
    )

    verified = engine.verify(record)
    assert verified.status == ConsumptionRecordStatus.VERIFIED

    rejected = engine.reject(record)
    assert rejected.status == ConsumptionRecordStatus.REJECTED