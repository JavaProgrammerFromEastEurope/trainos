from dataclasses import dataclass

from kernel.workflow.snapshot.execution_snapshot import ExecutionSnapshot
from kernel.workflow.snapshot.step_snapshot import StepSnapshot


@dataclass(frozen=True, slots=True)
class WorkflowSnapshot:

    snapshot_id: str

    workflow_id: str

    execution: ExecutionSnapshot
    steps: tuple[StepSnapshot, ...]
