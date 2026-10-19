from kernel.intelligence.cognition.cognition_registry import CognitionRegistry
from kernel.intelligence.cognition.cognition_snapshot import CognitionSnapshot
from kernel.intelligence.cognition.cognition_state import CognitionState


def test_cognition_registry_register():

    registry = CognitionRegistry()
    snapshot = CognitionSnapshot(
        state=CognitionState(
            awareness_level=1.0,
            coherence=1.0,
        )
    )
    registry.register(snapshot)
    assert registry.snapshots() == (snapshot,)
