from .delivery_job import DeliveryJob
from .delivery_job_result import DeliveryJobResult
from .delivery_job_status import DeliveryJobStatus


class DeliveryJobEngine:

    def execute(
        self,
        job: DeliveryJob,
    ) -> DeliveryJobResult:
        return DeliveryJobResult(
            job_id=job.job_id,
            status=DeliveryJobStatus.COMPLETED,
        )