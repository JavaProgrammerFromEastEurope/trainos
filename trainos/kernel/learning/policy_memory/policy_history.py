from __future__ import annotations

from .policy_version import (
    PolicyVersion,
)


class PolicyHistory:

    def __init__(
        self,
    ) -> None:
        self._versions: list[PolicyVersion] = []

    def add(
        self,
        version: PolicyVersion,
    ) -> None:
        self._versions.append(version)

    def versions(
        self,
    ) -> tuple[PolicyVersion, ...]:
        return tuple(self._versions)
