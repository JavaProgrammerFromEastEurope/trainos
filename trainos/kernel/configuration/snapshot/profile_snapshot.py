from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class ProfileSnapshot:

    active_profile: str
