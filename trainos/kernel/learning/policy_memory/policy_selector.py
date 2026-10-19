from .policy_version import (
    PolicyVersion,
)


class PolicySelector:

    def select(
        self,
        policies: list[PolicyVersion],
    ) -> PolicyVersion:
        return policies[-1]
