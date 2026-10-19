from kernel.constitution.validation.constitutional_validation import ConstitutionalValidation
from kernel.constitution.validation.validation_result import ValidationResult


def test_constitution_validation():

    validation = ConstitutionalValidation(
        proposal="Modify election procedure",
        result=ValidationResult.VALID,
        reason="No constitutional conflict",
    )

    assert validation.result == ValidationResult.VALID