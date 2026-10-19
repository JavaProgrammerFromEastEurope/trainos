from dataclasses import dataclass

from .production_job_status import ProductionJobStatus


@dataclass(frozen=True, slots=True)
class ProductionJobResult:

    job_id: str
    status: ProductionJobStatus