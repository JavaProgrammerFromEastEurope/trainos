from .policy_checkpoint import (
    PolicyCheckpoint,
)


class PolicyEngine:

    def checkpoint(
        self,
        version: int,
    ) -> PolicyCheckpoint:
        return PolicyCheckpoint(
            version=version,
        )
