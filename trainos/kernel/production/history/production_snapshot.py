from dataclasses import dataclass

from ..jobs.production_job_status import ProductionJobStatus


@dataclass(frozen=True, slots=True)
class ProductionSnapshot:

    snapshot_id: 	str
    job_id: 			str
    status: ProductionJobStatus