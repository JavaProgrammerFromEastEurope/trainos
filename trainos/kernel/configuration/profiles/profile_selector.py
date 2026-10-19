from .configuration_profile import ConfigurationProfile
from .profile_status import ProfileStatus


class ProfileSelector:

    def activate(
        self,
        profile: ConfigurationProfile,
    ) -> ConfigurationProfile:
        return ConfigurationProfile(
            profile_id=profile.profile_id,
            name=profile.name,
            status=ProfileStatus.ACTIVE,
        )
