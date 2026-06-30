from .authority import GovernanceAuthority


class GovernanceEngine:

    def authorize(
        self,
        authority: GovernanceAuthority,
    ) -> GovernanceAuthority:
        return authority
