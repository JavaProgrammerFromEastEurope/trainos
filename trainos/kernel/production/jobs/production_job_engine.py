from .production_job import ProductionJob
from .production_job_result import ProductionJobResult
from .production_job_status import ProductionJobStatus


class ProductionJobEngine:

    def execute(
        self,
        job: ProductionJob,
    ) -> ProductionJobResult:
        return ProductionJobResult(
            job_id=job.job_id,
            status=ProductionJobStatus.COMPLETED,
        )
