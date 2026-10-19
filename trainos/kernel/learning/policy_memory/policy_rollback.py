from .policy_version import (
    PolicyVersion,
)


class PolicyRollback:

    def rollback(
        self,
        version: PolicyVersion,
    ) -> PolicyVersion:
        return version
