from .negotiation_result import NegotiationResult


class NegotiationEngine:

    def negotiate(self) -> NegotiationResult:
        return NegotiationResult(accepted=True)
