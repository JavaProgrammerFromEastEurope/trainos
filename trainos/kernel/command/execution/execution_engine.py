from __future__ import annotations

from .command_execution import CommandExecution
from .execution_status import ExecutionStatus
from ..events import CommandEventService, ExecutionEventAdapter


class ExecutionEngine:
    """Immutable command-execution lifecycle transitions with optional events."""

    def __init__(self, event_service: CommandEventService | None = None) -> None:
        self._event_adapter = (
            ExecutionEventAdapter(event_service) if event_service is not None else None
        )

    def create(self, execution: CommandExecution, command_type: str = "command") -> CommandExecution:
        self._require_status(execution, ExecutionStatus.CREATED, "create")
        if self._event_adapter is not None:
            self._event_adapter.command_created(execution.command_id, command_type)
        return execution

    def start(self, execution: CommandExecution) -> CommandExecution:
        self._require_status(execution, ExecutionStatus.CREATED, "start")
        updated = self._replace_status(execution, ExecutionStatus.RUNNING)
        if self._event_adapter is not None:
            self._event_adapter.command_started(command_id=updated.command_id)
        return updated

    def complete(self, execution: CommandExecution) -> CommandExecution:
        self._require_status(execution, ExecutionStatus.RUNNING, "complete")
        updated = self._replace_status(execution, ExecutionStatus.COMPLETED)
        if self._event_adapter is not None:
            self._event_adapter.command_completed(
                command_id=updated.command_id,
                result={
                    "execution_id": updated.execution_id,
                    "progress": str(updated.progress),
                    "status": updated.status.value,
                },
            )
        return updated

    def fail(self, execution: CommandExecution, error_message: str) -> CommandExecution:
        self._require_statuses(
            execution, (ExecutionStatus.CREATED, ExecutionStatus.RUNNING), "fail"
        )
        if not isinstance(error_message, str) or not error_message.strip():
            raise ValueError("error_message must not be empty")
        updated = self._replace_status(execution, ExecutionStatus.FAILED)
        if self._event_adapter is not None:
            self._event_adapter.command_failed(
                command_id=updated.command_id, error_message=error_message
            )
        return updated

    @staticmethod
    def _replace_status(execution: CommandExecution, status: ExecutionStatus) -> CommandExecution:
        return CommandExecution(
            execution_id=execution.execution_id,
            command_id=execution.command_id,
            progress=execution.progress,
            status=status,
        )

    @staticmethod
    def _require_status(execution: CommandExecution, expected: ExecutionStatus, operation: str) -> None:
        ExecutionEngine._require_statuses(execution, (expected,), operation)

    @staticmethod
    def _require_statuses(
        execution: CommandExecution,
        expected: tuple[ExecutionStatus, ...],
        operation: str,
    ) -> None:
        if not isinstance(execution, CommandExecution):
            raise TypeError("execution must be a CommandExecution")
        if execution.status not in expected:
            allowed = ", ".join(status.value for status in expected)
            raise ValueError(
                f"cannot {operation} execution in {execution.status.value!r} state; expected {allowed}"
            )
