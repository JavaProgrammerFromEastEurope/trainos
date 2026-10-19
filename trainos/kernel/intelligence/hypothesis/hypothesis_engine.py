from .hypothesis import Hypothesis
from .hypothesis_status import HypothesisStatus


class HypothesisEngine:

    def generate(self, description: str) -> Hypothesis:
        return Hypothesis(
            description=description,
            status=HypothesisStatus.PROPOSED,
        )
