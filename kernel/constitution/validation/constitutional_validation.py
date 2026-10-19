from dataclasses import dataclass

from .validation_result import ValidationResult


@dataclass(frozen=True)
class ConstitutionalValidation:

    proposal: str
    result: ValidationResult
    reason: str