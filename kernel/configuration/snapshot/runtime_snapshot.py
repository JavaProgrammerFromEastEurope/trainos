from dataclasses import dataclass

from kernel.configuration.runtime.runtime_status import ConfigurationRuntimeStatus


@dataclass(frozen=True, slots=True)
class RuntimeSnapshot:

    runtime_id: str
    status: ConfigurationRuntimeStatus
