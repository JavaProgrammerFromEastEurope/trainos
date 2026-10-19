from dataclasses import dataclass

from .consumption_job_status import ConsumptionJobStatus


@dataclass(frozen=True, slots=True)
class ConsumptionJobResult:

    job_id: str
    status: ConsumptionJobStatus