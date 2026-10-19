from .reflection import Reflection
from .reflection_type import ReflectionType


class ReflectionEngine:

    def reflect(self) -> Reflection:
        return Reflection(type=ReflectionType.INTERNAL)
