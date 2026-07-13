from kernel.configuration.profiles.configuration_profile import ConfigurationProfile

from kernel.configuration.profiles.profile_status import ProfileStatus
from kernel.configuration.profiles.profile_engine import ProfileEngine


def test_profile_activation():

    profile = ConfigurationProfile(profile_id="DEV", name="Development")
    profile = ProfileEngine().activate(profile)
    assert profile.status == ProfileStatus.ACTIVE
