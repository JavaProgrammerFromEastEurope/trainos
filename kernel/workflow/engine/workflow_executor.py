from .execution_result import ExecutionResult


class WorkflowExecutor:

    def execute(
        self,
        workflow,
    ) -> ExecutionResult:
        return ExecutionResult(
            success=True,
            workflow_id=workflow.workflow_id,
        )
