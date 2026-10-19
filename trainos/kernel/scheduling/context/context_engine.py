from .execution_context import ExecutionContext

from .execution_state import ExecutionState


class ContextEngine:

    def activate(
        self,
        context: ExecutionContext,
    ) -> ExecutionContext:
        return ExecutionContext(
            task_id=context.task_id,
            metadata=context.metadata,
            state=ExecutionState.ACTIVE,
        )

    def finish(
        self,
        context: ExecutionContext,
    ) -> ExecutionContext:
        return ExecutionContext(
            task_id=context.task_id,
            metadata=context.metadata,
            state=ExecutionState.FINISHED,
        )
