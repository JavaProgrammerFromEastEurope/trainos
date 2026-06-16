from trainos.kernel.behavior.utility.utility_option import (
    UtilityOption,
)

from trainos.kernel.behavior.utility.utility_evaluator import (
    UtilityEvaluator,
)


def test_utility_ai():

    evaluator = UtilityEvaluator()
    result = evaluator.evaluate(
        [
            UtilityOption(name="attack", 		score=0.3),
            UtilityOption(name="explore", 	score=0.5),
            UtilityOption(name="recharge", 	score=0.9),
        ]
    )

    assert result.option == "recharge"
    assert result.score == 0.9
