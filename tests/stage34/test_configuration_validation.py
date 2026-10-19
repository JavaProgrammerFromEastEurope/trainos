from kernel.configuration.validation.validation_rule import ValidationRule

from kernel.configuration.validation.validation_engine import ValidationEngine


def test_configuration_validation():

    rule = ValidationRule(
        key="storage.backend",
    )
    result = ValidationEngine().validate("sqlite", rule)

    assert result.valid is True
