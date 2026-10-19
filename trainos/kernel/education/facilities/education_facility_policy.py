from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class EducationFacilityPolicy:

    allow_training: bool = True
    allow_shutdown: bool = True