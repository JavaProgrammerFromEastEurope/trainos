from kernel.core.registry.base_registry import BaseRegistry

from .configuration_definition import (
    ConfigurationDefinition,
)


class DefinitionRegistry(
    BaseRegistry[ConfigurationDefinition],
):
    pass
