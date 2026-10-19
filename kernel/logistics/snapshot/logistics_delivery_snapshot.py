from dataclasses import dataclass

from kernel.logistics.jobs.delivery_job_status import DeliveryJobStatus


@dataclass(frozen=True, slots=True)
class LogisticsDeliverySnapshot:

    job_id: str
    status: DeliveryJobStatus