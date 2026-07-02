from .amendment_proposal import AmendmentProposal


class AmendmentEngine:

    def submit(
        self,
        proposal: AmendmentProposal,
    ) -> AmendmentProposal:
        return proposal
