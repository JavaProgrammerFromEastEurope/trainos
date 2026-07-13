from kernel.core.registry.base_registry import BaseRegistry

from .configuration_provider import ConfigurationProvider


class ProviderRegistry(
    BaseRegistry[ConfigurationProvider],
):
    pass
