from kernel.configuration.definitions.configuration_definition import (
    ConfigurationDefinition,
)

from kernel.configuration.definitions.configuration_type import ConfigurationType
from kernel.configuration.values.configuration_value import ConfigurationValue
from kernel.configuration.values.value_status import ValueStatus
from kernel.configuration.values.value_engine import ValueEngine


def test_value_engine_update():

    definition = ConfigurationDefinition(
        key="simulation.tick_duration",
        value_type=ConfigurationType.FLOAT,
        description="Tick",
    )
    value = ConfigurationValue(
        definition=definition,
        value=1.0,
    )
    updated = ValueEngine().update(value, 0.25)

    assert updated.value == 0.25
    assert updated.status == ValueStatus.OVERRIDDEN
