from .configuration_definition import (
    ConfigurationDefinition,
)


class DefinitionEngine:

    def register(
        self,
        definition: ConfigurationDefinition,
    ) -> ConfigurationDefinition:
        return definition
