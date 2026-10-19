from .evaluation_result import (
    EvaluationResult,
)


class SelfAssessment:

    def evaluate(
        self,
    ) -> EvaluationResult:
        return EvaluationResult(
            success=True,
        )
