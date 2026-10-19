from kernel.strategy.preference.preference_dimension import PreferenceDimension
from kernel.strategy.preference.preference_profile import PreferenceProfile
from kernel.strategy.preference.preference_registry import PreferenceRegistry
from kernel.strategy.preference.preference_weight import PreferenceWeight


def test_preference_registry_register():

    registry = PreferenceRegistry()
    profile = PreferenceProfile(
        weights=(
            PreferenceWeight(
                dimension=PreferenceDimension.SURVIVAL,
                weight=1.0,
            ),
        ),
    )
    registry.register(profile)
    assert registry.profiles() == (profile,)
