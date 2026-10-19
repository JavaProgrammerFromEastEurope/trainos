from dataclasses import dataclass

from .execution_progress import ExecutionProgress
from .execution_status import ExecutionStatus


@dataclass(frozen=True, slots=True)
class CommandExecution:
    """Immutable execution record for a command."""

    execution_id: str
    command_id: str
    progress: ExecutionProgress
    status: ExecutionStatus = ExecutionStatus.CREATED

    def __post_init__(self) -> None:
        if not self.execution_id.strip():
            raise ValueError("execution_id must not be empty")
        if not self.command_id.strip():
            raise ValueError("command_id must not be empty")
        if not isinstance(self.progress, ExecutionProgress):
            raise TypeError("progress must be an ExecutionProgress")
        if not isinstance(self.status, ExecutionStatus):
            raise TypeError("status must be an ExecutionStatus")
