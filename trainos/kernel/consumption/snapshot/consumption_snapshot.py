from dataclasses import dataclass

from .consumer_snapshot import ConsumerSnapshot
from .consumption_job_snapshot 			import ConsumptionJobSnapshot
from .consumption_record_snapshot 	import ConsumptionRecordSnapshot
from .consumption_request_snapshot 	import ConsumptionRequestSnapshot
from .consumption_runtime_snapshot 	import ConsumptionRuntimeSnapshot


@dataclass(frozen=True, slots=True)
class ConsumptionSnapshot:

    snapshot_id: str
    runtime: ConsumptionRuntimeSnapshot
    consumers: 	tuple[ConsumerSnapshot, ...]
    requests: 	tuple[ConsumptionRequestSnapshot, ...]
    jobs: 			tuple[ConsumptionJobSnapshot, ...]
    records: 		tuple[ConsumptionRecordSnapshot, ...]
