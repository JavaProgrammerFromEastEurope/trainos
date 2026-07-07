from dataclasses import dataclass

from .production_job_status import ProductionJobStatus


@dataclass(frozen=True, slots=True)
class ProductionJob:

    job_id: 		str
    recipe_id: 	str
    factory_id: str
    status: ProductionJobStatus