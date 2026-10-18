from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from enum import Enum


def _normalize(value: str | Enum) -> str:
    """Convert strings and enum values into a stable representation."""
    if isinstance(value, Enum):
        value = value.value

    return str(value)


@dataclass(frozen=True, slots=True)
class CommandSnapshot:
    """Immutable diagnostic snapshot of a command execution."""

    command_id: str
    command_type: str
    command_state: str
    attempt_count: int
    execution_status: str
    active_handler: str | None
    timestamp: datetime
    error_message: str | None = None

    def __post_init__(self) -> None:
        if not self.command_id:
            raise ValueError("command_id must not be empty")

        if not self.command_type:
            raise ValueError("command_type must not be empty")

        if self.attempt_count < 0:
            raise ValueError("attempt_count must not be negative")

        if self.timestamp.tzinfo is None or self.timestamp.utcoffset() is None:
            raise ValueError("timestamp must be timezone-aware")

    @classmethod
    def create(
        cls,
        *,
        command_id: str,
        command_type: str,
        command_state: str | Enum,
        attempt_count: int,
        execution_status: str | Enum,
        active_handler: str | None = None,
        error_message: str | None = None,
    ) -> CommandSnapshot:
        """Create a snapshot from the current execution data."""
        return cls(
            command_id=command_id,
            command_type=command_type,
            command_state=_normalize(command_state),
            attempt_count=attempt_count,
            execution_status=_normalize(execution_status),
            active_handler=active_handler,
            timestamp=datetime.now(timezone.utc),
            error_message=error_message,
        )

    def to_dict(self) -> dict[str, str | int | None]:
        """Return a JSON-friendly representation."""
        return {
            "command_id": self.command_id,
            "command_type": self.command_type,
            "command_state": self.command_state,
            "attempt_count": self.attempt_count,
            "execution_status": self.execution_status,
            "active_handler": self.active_handler,
            "timestamp": self.timestamp.isoformat(),
            "error_message": self.error_message,
        }
