from kernel.workflow.context.workflow_context import WorkflowContext

from kernel.workflow.context.workflow_metadata 	import WorkflowMetadata
from kernel.workflow.context.context_engine 		import ContextEngine
from kernel.workflow.context.context_state 			import ContextState


def test_workflow_context():

    context = WorkflowContext(
        workflow_id="WF-005",
        metadata=WorkflowMetadata(
            runtime_id="RUN-001",
            scheduler_id="SCH-001",
            tick=150,
            correlation_id="CORR-001",
        ),
    )
    context = ContextEngine().activate(context)

    assert context.state == ContextState.ACTIVE
    assert context.metadata.tick == 150
    assert context.metadata.runtime_id == "RUN-001"
