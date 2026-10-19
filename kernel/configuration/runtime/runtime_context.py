from dataclasses import dataclass

from kernel.configuration.providers.provider_engine import ProviderEngine


@dataclass(slots=True)
class RuntimeContext:

    provider_engine: ProviderEngine
