from dataclasses import dataclass


@dataclass(frozen=True)
class ReflectionPolicy:

    allow_reflection: bool