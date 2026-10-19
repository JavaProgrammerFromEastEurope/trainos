from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class ValidationResult:

    valid: 		bool
    message: 	str = ""