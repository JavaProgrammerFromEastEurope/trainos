from __future__ import annotations

from .rule import Rule


class RuleSet:

    def __init__(self) -> None:
        self._rules: list[Rule] = []

    def add(
        self,
        rule: Rule,
    ) -> None:
        self._rules.append(
            rule,
        )

    def all(
        self,
    ) -> list[Rule]:
        return self._rules
