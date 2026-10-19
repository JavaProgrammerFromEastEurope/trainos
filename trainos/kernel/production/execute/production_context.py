from dataclasses import dataclass


@dataclass(slots=True)
class ProductionContext:

    factory_id: str
    job_id: 		str
    recipe_id: 	str