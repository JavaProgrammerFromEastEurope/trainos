from kernel.configuration.validation.validation_rule import (
    ValidationRule,
)

from kernel.configuration.validation.validation_engine import (
    ValidationEngine,
)


def test_configuration_validation_failure():

    rule 		= ValidationRule(key="simulation.tick_duration")
    result 	= ValidationEngine().validate(None, rule)

    assert result.valid is False
    assert result.message == "Missing configuration value"
