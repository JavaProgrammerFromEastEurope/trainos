from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class ProductionJobRequest:

    job_id: 		str
    recipe_id: 	str
    factory_id: str