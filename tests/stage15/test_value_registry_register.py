from kernel.strategy.value.value_assessment import ValueAssessment
from kernel.strategy.value.value_dimension import ValueDimension
from kernel.strategy.value.value_registry import ValueRegistry
from kernel.strategy.value.value_score import ValueScore


def test_value_registry_register():

    registry = ValueRegistry()
    assessment = ValueAssessment(
        outcome="food increase",
        scores=(
            ValueScore(
                dimension=ValueDimension.SURVIVAL,
                score=0.9,
            ),
        ),
    )
    registry.register(assessment)
    assert registry.assessments() == (assessment,)
