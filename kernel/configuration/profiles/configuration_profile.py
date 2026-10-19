from dataclasses import dataclass

from .profile_status import ProfileStatus


@dataclass(frozen=True, slots=True)
class ConfigurationProfile:

    profile_id: str
    name: str
    status: ProfileStatus = ProfileStatus.INACTIVE