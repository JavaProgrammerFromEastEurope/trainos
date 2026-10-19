from dataclasses import dataclass

from .configuration_type import ConfigurationType


@dataclass(frozen=True, slots=True)
class ConfigurationDefinition:

    key: 					str
    value_type: ConfigurationType
    description: 	str