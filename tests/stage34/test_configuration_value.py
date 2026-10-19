from kernel.configuration.definitions.configuration_definition import (
    ConfigurationDefinition,
)

from kernel.configuration.definitions.configuration_type import ConfigurationType
from kernel.configuration.values.configuration_value import ConfigurationValue
from kernel.configuration.values.value_status import ValueStatus


def test_configuration_value():

    definition = ConfigurationDefinition(
        key="population.max_population",
        value_type=ConfigurationType.INTEGER,
        description="Maximum population",
    )
    value = ConfigurationValue(
        definition=definition,
        value=5000,
    )

    assert value.value == 5000
    assert value.status == ValueStatus.DEFAULT
