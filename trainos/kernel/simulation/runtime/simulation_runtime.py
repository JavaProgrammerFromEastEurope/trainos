from dataclasses import dataclass

from .runtime_status import RuntimeStatus


@dataclass(frozen=True, slots=True)
class SimulationRuntime:

    runtime_id: str
    status: RuntimeStatus