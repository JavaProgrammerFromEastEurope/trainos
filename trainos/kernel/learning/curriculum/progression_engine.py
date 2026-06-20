from .mastery_result import MasteryResult


class ProgressionEngine:

    def evaluate(
        self,
    ) -> MasteryResult:
        return MasteryResult(mastered=True)
