from .inference_result import InferenceResult


class InferenceEngine:

    def infer(self) -> InferenceResult:
        return InferenceResult(
            conclusion="derived knowledge",
        )
