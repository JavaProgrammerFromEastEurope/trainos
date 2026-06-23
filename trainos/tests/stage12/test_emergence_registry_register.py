from trainos.kernel.metacivilization.emergence.emergence_registry import EmergenceRegistry
from trainos.kernel.metacivilization.emergence.emergence_pattern import EmergencePattern


def test_emergence_registry_register():

    registry = EmergenceRegistry()
    pattern = EmergencePattern(
        name="cooperation",
        stability=0.9,
    )
    registry.register(pattern)
    assert registry.patterns() == (pattern,)