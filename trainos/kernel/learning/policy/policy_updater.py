from __future__ import annotations

from .policy import (
    Policy,
)


class PolicyUpdater:

    def update(
        self,
        policy: Policy,
    ) -> Policy:
        return policy
