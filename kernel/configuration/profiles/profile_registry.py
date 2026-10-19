from kernel.core.registry.base_registry import BaseRegistry

from .configuration_profile import ConfigurationProfile


class ProfileRegistry(
    BaseRegistry[ConfigurationProfile],
):
    pass
