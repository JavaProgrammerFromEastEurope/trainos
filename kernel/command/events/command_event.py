from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any
from uuid import uuid4

from .event_type import CommandEventType


@dataclass(frozen=True, slots=True)
class CommandEvent:
    """Immutable envelope for a command lifecycle event."""

    event_id: str
    command_id: str
    event_type: CommandEventType
    timestamp: datetime
    payload: dict[str, Any]

    def __post_init__(self) -> None:
        if not self.event_id.strip():
            raise ValueError("event_id must not be empty")
        if not self.command_id.strip():
            raise ValueError("command_id must not be empty")
        if not isinstance(self.event_type, CommandEventType):
            raise TypeError("event_type must be a CommandEventType")
        if self.timestamp.tzinfo is None or self.timestamp.utcoffset() is None:
            raise ValueError("timestamp must be timezone-aware")
        if not isinstance(self.payload, dict):
            raise TypeError("payload must be a dict")

    @classmethod
    def create(
        cls,
        command_id: str,
        event_type: CommandEventType,
        payload: dict[str, Any] | None = None,
    ) -> CommandEvent:
        if not command_id or not command_id.strip():
            raise ValueError("command_id must not be empty")
        if not isinstance(event_type, CommandEventType):
            raise TypeError("event_type must be a CommandEventType")
        return cls(
            event_id=str(uuid4()),
            command_id=command_id,
            event_type=event_type,
            timestamp=datetime.now(timezone.utc),
            payload=dict(payload) if payload is not None else {},
        )
