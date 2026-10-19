from .consumption_job import ConsumptionJob
from .consumption_job_result import ConsumptionJobResult
from .consumption_job_status import ConsumptionJobStatus


class ConsumptionJobEngine:

    def execute(
        self,
        job: ConsumptionJob,
    ) -> ConsumptionJobResult:
        return ConsumptionJobResult(
            job_id=job.job_id,
            status=ConsumptionJobStatus.COMPLETED,
        )