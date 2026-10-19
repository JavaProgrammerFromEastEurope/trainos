from __future__ import annotations

from .constitutional_rule import ConstitutionalRule


class ConstitutionRegistry:

    def __init__(self) -> None:
        self._rules: list[ConstitutionalRule] = []

    def register(self, rule: ConstitutionalRule) -> None:
        self._rules.append(rule)

    def rules(self) -> tuple[ConstitutionalRule, ...]:
        return tuple(self._rules)
