from dataclasses import dataclass

from .delivery_job_status import DeliveryJobStatus


@dataclass(frozen=True, slots=True)
class DeliveryJobResult:

    job_id: str
    status: DeliveryJobStatus