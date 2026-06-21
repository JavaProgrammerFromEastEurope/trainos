from __future__ import annotations

from .routing_rule import RoutingRule


class RoutingTable:

    def __init__(self) -> None:
        self._rules: list[RoutingRule] = []

    def add(self, rule: RoutingRule) -> None:
        self._rules.append(rule)

    def rules(self) -> tuple[RoutingRule, ...]:
        return tuple(self._rules)