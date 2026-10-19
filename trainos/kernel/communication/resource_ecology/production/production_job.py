from dataclasses import dataclass

from .production_recipe import ProductionRecipe


@dataclass
class ProductionJob:

    recipe: ProductionRecipe
