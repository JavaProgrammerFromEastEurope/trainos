from __future__ import annotations

from .policy_version import (
    PolicyVersion,
)


class PolicyRegistry:

    def __init__(
        self,
    ) -> None:
        self._current = PolicyVersion(version=1)

    @property
    def current(
        self,
    ) -> PolicyVersion:
        return self._current
