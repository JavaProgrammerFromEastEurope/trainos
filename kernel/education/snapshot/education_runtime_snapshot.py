from dataclasses import dataclass

from kernel.education.runtime.education_lifecycle import (
    EducationLifecycle,
)


@dataclass(frozen=True, slots=True)
class EducationRuntimeSnapshot:

    lifecycle: EducationLifecycle
