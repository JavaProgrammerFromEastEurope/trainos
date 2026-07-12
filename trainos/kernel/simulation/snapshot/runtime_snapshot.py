from dataclasses import dataclass

from kernel.simulation.runtime.runtime_status import RuntimeStatus


@dataclass(frozen=True, slots=True)
class RuntimeSnapshot:

    runtime_id: str
    status: RuntimeStatus
