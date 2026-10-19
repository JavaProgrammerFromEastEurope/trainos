from .workflow_context 	import WorkflowContext
from .context_state 		import ContextState


class ContextEngine:

    def activate(
        self,
        context: WorkflowContext,
    ) -> WorkflowContext:
        return WorkflowContext(
            workflow_id=context.workflow_id,
            metadata=context.metadata,
            state=ContextState.ACTIVE,
        )

    def close(
        self,
        context: WorkflowContext,
    ) -> WorkflowContext:
        return WorkflowContext(
            workflow_id=context.workflow_id,
            metadata=context.metadata,
            state=ContextState.CLOSED,
        )
