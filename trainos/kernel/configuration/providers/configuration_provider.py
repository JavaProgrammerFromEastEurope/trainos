from dataclasses import dataclass

from .provider_type import ProviderType


@dataclass(frozen=True, slots=True)
class ConfigurationProvider:

    provider_id: str
    provider_type: ProviderType