from .consumption_record import ConsumptionRecord
from .consumption_record_status import ConsumptionRecordStatus


class ConsumptionRecordEngine:

    def verify(
        self,
        record: ConsumptionRecord,
    ) -> ConsumptionRecord:
        return ConsumptionRecord(
            record_id=record.record_id,
            consumer_id=record.consumer_id,
            resource_id=record.resource_id,
            quantity=record.quantity,
            status=ConsumptionRecordStatus.VERIFIED,
        )

    def reject(
        self,
        record: ConsumptionRecord,
    ) -> ConsumptionRecord:
        return ConsumptionRecord(
            record_id=record.record_id,
            consumer_id=record.consumer_id,
            resource_id=record.resource_id,
            quantity=record.quantity,
            status=ConsumptionRecordStatus.REJECTED,
        )
