from __future__ import annotations

from typing import Any

from .command_event import CommandEvent
from .event_service import CommandEventService
from .event_type import CommandEventType


class ExecutionEventAdapter:
    """Publishes lifecycle events for command execution."""

    def __init__(self, event_service: CommandEventService) -> None:
        self._event_service = event_service

    def command_created(
        self,
        command_id: str,
        command_type: str,
    ) -> CommandEvent:
        return self._publish(
            command_id,
            CommandEventType.COMMAND_CREATED,
            {"command_type": command_type},
        )

    def command_started(
        self,
        command_id: str,
        handler: str | None = None,
    ) -> CommandEvent:
        return self._publish(
            command_id,
            CommandEventType.COMMAND_STARTED,
            {"handler": handler},
        )

    def progress_updated(
        self,
        command_id: str,
        attempts: int,
        max_attempts: int,
        completed: bool,
    ) -> CommandEvent:
        if attempts < 0:
            raise ValueError("attempts must not be negative")
        if max_attempts < 1:
            raise ValueError("max_attempts must be positive")
        if attempts > max_attempts:
            raise ValueError("attempts cannot exceed max_attempts")
        return self._publish(
            command_id,
            CommandEventType.COMMAND_PROGRESS_UPDATED,
            {
                "attempts": attempts,
                "max_attempts": max_attempts,
                "completed": completed,
            },
        )

    def command_retrying(
        self,
        command_id: str,
        attempt: int,
        reason: str | None = None,
    ) -> CommandEvent:
        if attempt < 1:
            raise ValueError("attempt must be positive")
        return self._publish(
            command_id,
            CommandEventType.COMMAND_RETRYING,
            {"attempt": attempt, "reason": reason},
        )

    def command_completed(
        self,
        command_id: str,
        result: Any = None,
    ) -> CommandEvent:
        return self._publish(
            command_id,
            CommandEventType.COMMAND_COMPLETED,
            {"result": result},
        )

    def command_failed(
        self,
        command_id: str,
        error_message: str,
        attempt: int | None = None,
    ) -> CommandEvent:
        return self._publish(
            command_id,
            CommandEventType.COMMAND_FAILED,
            {
                "error_message": error_message,
                "attempt": attempt,
            },
        )

    def command_cancelled(
        self,
        command_id: str,
        reason: str | None = None,
    ) -> CommandEvent:
        return self._publish(
            command_id,
            CommandEventType.COMMAND_CANCELLED,
            {"reason": reason},
        )

    def _publish(
        self,
        command_id: str,
        event_type: CommandEventType,
        payload: dict[str, Any],
    ) -> CommandEvent:
        return self._event_service.publish(
            command_id=command_id,
            event_type=event_type,
            payload=payload,
        )
