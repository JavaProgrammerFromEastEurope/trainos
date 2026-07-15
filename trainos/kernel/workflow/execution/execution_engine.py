from .workflow_execution import WorkflowExecution
from .execution_status import ExecutionStatus


class ExecutionEngine:

    def start(
        self,
        execution: WorkflowExecution,
    ) -> WorkflowExecution:
        return WorkflowExecution(
            execution_id=execution.execution_id,
            workflow_id=execution.workflow_id,
            progress=execution.progress,
            status=ExecutionStatus.RUNNING,
        )

    def complete(
        self,
        execution: WorkflowExecution,
    ) -> WorkflowExecution:
        return WorkflowExecution(
            execution_id=execution.execution_id,
            workflow_id=execution.workflow_id,
            progress=execution.progress,
            status=ExecutionStatus.COMPLETED,
        )
