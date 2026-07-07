from dataclasses import dataclass

from .recipe_input 	import RecipeInput
from .recipe_output import RecipeOutput


@dataclass(frozen=True, slots=True)
class ProductionRecipe:

    recipe_id: 			str
    production_id: 	str
    inputs: 	tuple[RecipeInput, ...]
    outputs: 	tuple[RecipeOutput, ...]