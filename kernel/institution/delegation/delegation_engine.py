from .institutional_delegation import InstitutionalDelegation


class DelegationEngine:

    def delegate(
        self,
        delegation: InstitutionalDelegation,
    ) -> InstitutionalDelegation:
        return delegation