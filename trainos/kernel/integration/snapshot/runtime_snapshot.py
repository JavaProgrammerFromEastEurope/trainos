from dataclasses import dataclass

from kernel.integration.runtime.runtime_status import IntegrationRuntimeStatus


@dataclass(frozen=True, slots=True)
class IntegrationRuntimeSnapshot:

    runtime_id: str
    status: IntegrationRuntimeStatus
