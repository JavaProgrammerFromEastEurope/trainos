from dataclasses import dataclass

from .guardian_status import GuardianStatus


@dataclass(frozen=True)
class ConstitutionalGuardian:

    name: str
    status: GuardianStatus