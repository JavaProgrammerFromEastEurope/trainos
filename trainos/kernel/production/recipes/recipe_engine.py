from .production_recipe import ProductionRecipe


class RecipeEngine:

    def validate(
        self,
        recipe: ProductionRecipe,
    ) -> ProductionRecipe:
        return recipe
