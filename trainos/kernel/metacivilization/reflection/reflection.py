from dataclasses import dataclass

from .reflection_type import ReflectionType


@dataclass
class Reflection:

    type: ReflectionType
