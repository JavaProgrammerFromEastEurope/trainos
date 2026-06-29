from trainos.kernel.intelligence.hypothesis.hypothesis import Hypothesis
from trainos.kernel.intelligence.hypothesis.hypothesis_registry import (
    HypothesisRegistry,
)
from trainos.kernel.intelligence.hypothesis.hypothesis_status import HypothesisStatus


def test_hypothesis_registry_register():

    registry = HypothesisRegistry()
    hypothesis = Hypothesis(
        description="pump failure",
        status=HypothesisStatus.PROPOSED,
    )
    registry.register(hypothesis)
    assert registry.hypotheses() == (hypothesis,)
