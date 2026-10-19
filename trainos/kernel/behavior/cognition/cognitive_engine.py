from .cognitive_result import (
    CognitiveResult,
)


class CognitiveEngine:

    def step(
        self,
    ) -> CognitiveResult:
        return CognitiveResult(
            success=True,
        )
