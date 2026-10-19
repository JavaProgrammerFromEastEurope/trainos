from .validation_result import ValidationResult


class Validator:

    def validate(self, value, rule) -> ValidationResult:
        if rule.required and value is None:
            return ValidationResult(
                valid=False,
                message="Missing configuration value",
            )
        return ValidationResult(valid=True)
