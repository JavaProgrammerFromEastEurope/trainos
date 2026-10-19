from dataclasses import dataclass

from .runtime_status import IntegrationRuntimeStatus


@dataclass(frozen=True, slots=True)
class IntegrationRuntime:

    runtime_id: str
    status: IntegrationRuntimeStatus
