from kernel.simulation.definitions.simulation_definition 	import SimulationDefinition
from kernel.simulation.definitions.simulation_type 				import SimulationType
from kernel.simulation.definitions.simulation_category 		import SimulationCategory


def test_simulation_definition():

    definition = SimulationDefinition(
        simulation_id="SIM1",
        name="Civilization Simulation",
        simulation_type=SimulationType.CIVILIZATION,
        category=SimulationCategory.GLOBAL,
    )

    assert definition.simulation_id == "SIM1"
    assert definition.name == "Civilization Simulation"
    assert definition.simulation_type == SimulationType.CIVILIZATION
    assert definition.category == SimulationCategory.GLOBAL
