from dataclasses import dataclass

from .context_state import ContextState
from .workflow_metadata import WorkflowMetadata


@dataclass(frozen=True, slots=True)
class WorkflowContext:

    workflow_id: 	str
    metadata: 		WorkflowMetadata
    state: ContextState = ContextState.CREATED