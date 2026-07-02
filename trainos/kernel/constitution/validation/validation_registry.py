from __future__ import annotations

from .constitutional_validation import ConstitutionalValidation


class ValidationRegistry:

    def __init__(self) -> None:
        self._entries: list[ConstitutionalValidation] = []

    def register(self, validation: ConstitutionalValidation) -> None:
        self._entries.append(validation)

    def entries(self) -> tuple[ConstitutionalValidation, ...]:
        return tuple(self._entries)
