from __future__ import annotations

from .policy import Policy


class PolicyRegistry:

    def __init__(self) -> None:
        self._policies: list[Policy] = []

    def add(self, policy: Policy) -> None:
        self._policies.append(policy)

    def policies(self) -> tuple[Policy, ...]:
        return tuple(self._policies)
