from trainos.kernel.metacivilization.reflection.reflection import Reflection
from trainos.kernel.metacivilization.reflection.reflection_type import ReflectionType
from trainos.kernel.metacivilization.reflection.reflection_registry import ReflectionRegistry


def test_reflection_registry_add():

    registry = ReflectionRegistry()

    reflection = Reflection(
        type=ReflectionType.INTERNAL,
    )

    registry.add(reflection)

    assert registry.reflections() == (reflection,)