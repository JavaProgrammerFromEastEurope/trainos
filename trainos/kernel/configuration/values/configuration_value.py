from dataclasses import dataclass

from kernel.configuration.definitions.configuration_definition import (
    ConfigurationDefinition,
)

from .value_status import ValueStatus


@dataclass(frozen=True, slots=True)
class ConfigurationValue:

    definition: ConfigurationDefinition
    value: object
    status: ValueStatus = ValueStatus.DEFAULT
