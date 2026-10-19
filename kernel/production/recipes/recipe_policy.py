from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class RecipePolicy:

    allow_fractional_quantities: 	bool
    require_exact_inputs: 				bool