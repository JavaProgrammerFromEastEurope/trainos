from .configuration_value import ConfigurationValue


class ValueEngine:

    def update(
        self,
        configuration: ConfigurationValue,
        value: object,
    ) -> ConfigurationValue:
        return ConfigurationValue(
            definition=configuration.definition,
            value=value,
            status=configuration.status.OVERRIDDEN,
        )
