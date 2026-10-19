
from __future__ import annotations

from .command_execution import (
    CommandExecution,
)
from .execution_status import (
    ExecutionStatus,
)
from ..events import (
    CommandEventService,
    ExecutionEventAdapter,
)


class ExecutionEngine:
    def __init__(
        self,
        event_service: CommandEventService | None = None,
    ) -> None:
        self._event_adapter = (
            ExecutionEventAdapter(event_service)
            if event_service is not None
            else None
        )

    def start(
        self,
        execution: CommandExecution,
    ) -> CommandExecution:
        updated_execution = CommandExecution(
            execution_id=execution.execution_id,
            command_id=execution.command_id,
            progress=execution.progress,
            status=ExecutionStatus.RUNNING,
        )

        if self._event_adapter is not None:
            self._event_adapter.command_started(
                command_id=updated_execution.command_id,
            )
        return updated_execution

    def complete(
        self,
        execution: CommandExecution,
    ) -> CommandExecution:
        updated_execution = CommandExecution(
            execution_id=execution.execution_id,
            command_id=execution.command_id,
            progress=execution.progress,
            status=ExecutionStatus.COMPLETED,
        )
        if self._event_adapter is not None:
            self._event_adapter.command_completed(
                command_id=updated_execution.command_id,
                result={
                    "execution_id": updated_execution.execution_id,
                    "progress": str(updated_execution.progress),
                    "status": updated_execution.status.value,
                },
            )
        return updated_execution
