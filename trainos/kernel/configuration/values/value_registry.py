from kernel.core.registry.base_registry import BaseRegistry

from .configuration_value import ConfigurationValue


class ValueRegistry(
    BaseRegistry[ConfigurationValue],
):
    pass
