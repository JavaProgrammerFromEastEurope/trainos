from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class ProductionPolicy:

    require_factory_active: 	bool = True
    require_valid_recipe: 		bool = True
    allow_partial_execution: 	bool = False