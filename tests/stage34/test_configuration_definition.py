from kernel.configuration.definitions.configuration_definition import (
    ConfigurationDefinition,
)

from kernel.configuration.definitions.configuration_type import ConfigurationType


def test_configuration_definition():

    definition = ConfigurationDefinition(
        key="simulation.tick_duration",
        value_type=ConfigurationType.FLOAT,
        description="Simulation tick duration",
    )
    assert definition.key == "simulation.tick_duration"
    assert definition.value_type == ConfigurationType.FLOAT
    assert definition.description == "Simulation tick duration"
