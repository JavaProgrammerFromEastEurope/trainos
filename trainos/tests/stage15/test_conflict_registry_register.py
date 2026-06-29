from trainos.kernel.strategy.preference.preference_dimension import PreferenceDimension
from trainos.kernel.strategy.preference.preference_weight import PreferenceWeight
from trainos.kernel.strategy.preference_conflict.conflict_registry import (
    ConflictRegistry,
)
from trainos.kernel.strategy.preference_conflict.conflict_resolution import (
    PreferenceResolution,
)


def test_conflict_registry_register():

    registry = ConflictRegistry()
    resolution = PreferenceResolution(
        winner=PreferenceWeight(
            dimension=PreferenceDimension.SURVIVAL,
            weight=1.0,
        ),
    )
    registry.register(resolution)
    assert registry.resolutions() == (resolution,)
