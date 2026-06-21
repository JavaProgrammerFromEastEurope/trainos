from .trust_score import (
    TrustScore,
)


class TrustEngine:

    def evaluate(self) -> TrustScore:
        return TrustScore(value=1.0)
