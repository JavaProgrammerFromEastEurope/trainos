from dataclasses import dataclass

from .runtime_status import ConfigurationRuntimeStatus


@dataclass(frozen=True, slots=True)
class ConfigurationRuntime:

    runtime_id: str
    status: ConfigurationRuntimeStatus
