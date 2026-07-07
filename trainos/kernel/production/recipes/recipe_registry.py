from ...core.registry.base_registry import BaseRegistry

from .production_recipe import ProductionRecipe


class RecipeRegistry(
    BaseRegistry[ProductionRecipe],
):
    pass
