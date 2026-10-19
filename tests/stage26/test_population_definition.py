from kernel.population.definitions.population_category import PopulationCategory
from kernel.population.definitions.population_definition import PopulationDefinition
from kernel.population.definitions.population_type import PopulationType


def test_population_definition():

    definition = PopulationDefinition(
        population_id="citizen",
        name="Citizen",
        population_type=PopulationType.HUMAN,
        category=PopulationCategory.CIVILIAN,
    )

    assert definition.population_id == "citizen"
    assert definition.name == "Citizen"
    assert definition.population_type == PopulationType.HUMAN
    assert definition.category == PopulationCategory.CIVILIAN