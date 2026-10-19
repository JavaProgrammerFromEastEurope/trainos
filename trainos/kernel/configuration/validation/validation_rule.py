from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class ValidationRule:

    key: 			str
    required: bool = True