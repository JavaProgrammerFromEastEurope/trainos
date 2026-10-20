from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True, slots=True)
class CommandDispatchResult:
    """Unified outcome for routing and executing one command."""

    success: bool
    command_id: str
    handler_id: str | None = None
    output: Any = None
    error: str | None = None
    phase: str = "execution"

    def __post_init__(self) -> None:
        if not isinstance(self.success, bool):
            raise TypeError("success must be a bool")
        if not isinstance(self.command_id, str) or not self.command_id.strip():
            raise ValueError("command_id must not be empty")
        if self.handler_id is not None and (
            not isinstance(self.handler_id, str) or not self.handler_id.strip()
        ):
            raise ValueError("handler_id must be a non-empty string when provided")
        if not isinstance(self.phase, str) or not self.phase.strip():
            raise ValueError("phase must not be empty")
        if self.success and self.error is not None:
            raise ValueError("successful dispatch must not contain an error")
        if not self.success and (not isinstance(self.error, str) or not self.error.strip()):
            raise ValueError("failed dispatch requires a diagnostic error")
        if not self.success and self.output is not None:
            raise ValueError("failed dispatch must not contain output")
