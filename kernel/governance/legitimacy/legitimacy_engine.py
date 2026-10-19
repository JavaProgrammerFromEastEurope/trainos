from .governance_legitimacy import GovernanceLegitimacy


class LegitimacyEngine:

    def validate(
        self,
        legitimacy: GovernanceLegitimacy,
    ) -> GovernanceLegitimacy:
        return legitimacy
