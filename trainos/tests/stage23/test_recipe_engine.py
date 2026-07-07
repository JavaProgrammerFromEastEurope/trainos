from decimal import Decimal

from kernel.production.recipes.production_recipe import ProductionRecipe
from kernel.production.recipes.recipe_engine import RecipeEngine
from kernel.production.recipes.recipe_input import RecipeInput
from kernel.production.recipes.recipe_output import RecipeOutput


def test_recipe_engine():

    engine = RecipeEngine()

    recipe = ProductionRecipe(
        recipe_id="recipe1",
        production_id="water",
        inputs=(
            RecipeInput(
                resource_id="raw_water",
                quantity=Decimal("10"),
            ),
        ),
        outputs=(
            RecipeOutput(
                resource_id="clean_water",
                quantity=Decimal("10"),
            ),
        ),
    )

    result = engine.validate(recipe)

    assert result is recipe