from dataclasses import dataclass

from .engine_status import EngineStatus


@dataclass(frozen=True, slots=True)
class WorkflowEngine:

    engine_id: str
    status: EngineStatus = EngineStatus.READY