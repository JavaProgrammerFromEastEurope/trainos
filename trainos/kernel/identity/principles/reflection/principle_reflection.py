from dataclasses import dataclass

from .reflection_status import ReflectionStatus


@dataclass(frozen=True)
class PrincipleReflection:

    principle_name: str
    status: ReflectionStatus
    reason: 				str