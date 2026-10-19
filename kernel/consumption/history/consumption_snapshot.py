from dataclasses import dataclass

from kernel.consumption.jobs.consumption_job_status import ConsumptionJobStatus


@dataclass(frozen=True, slots=True)
class ConsumptionSnapshot:

    snapshot_id: str
    job_id: str
    status: ConsumptionJobStatus