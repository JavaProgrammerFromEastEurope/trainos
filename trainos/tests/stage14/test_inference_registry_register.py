from trainos.kernel.intelligence.inference.inference_registry import InferenceRegistry
from trainos.kernel.intelligence.inference.inference_result import InferenceResult


def test_inference_registry_register():

    registry = InferenceRegistry()
    result = InferenceResult(
        conclusion="future shortage",
    )
    registry.register(result)
    assert registry.results() == (result,)
