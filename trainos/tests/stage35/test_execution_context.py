from kernel.scheduling.context.execution_context import ExecutionContext

from kernel.scheduling.context.execution_metadata import ExecutionMetadata
from kernel.scheduling.context.context_engine 		import ContextEngine
from kernel.scheduling.context.execution_state 		import ExecutionState


def test_execution_context():
    context = ExecutionContext(
        task_id="TASK-007",
        metadata=ExecutionMetadata(
            scheduler_id="SCH-1",
            runtime_id="RUN-1",
            tick=10,
        ),
    )

    context = ContextEngine().activate(context)
    assert context.state == ExecutionState.ACTIVE
    assert context.metadata.tick == 10
