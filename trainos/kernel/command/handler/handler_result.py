from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True, slots=True)
class HandlerResult:
    """Outcome of one handler invocation.

    ``output`` is the callback's return value on success. ``error`` is a
    diagnostic message on failure and is intentionally absent on success.
    """

    success: bool
    command_id: str
    output: Any = None
    error: str | None = None

    def __post_init__(self) -> None:
        if not isinstance(self.success, bool):
            raise TypeError("success must be a bool")
        if not isinstance(self.command_id, str) or not self.command_id.strip():
            raise ValueError("command_id must not be empty")
        if self.success and self.error is not None:
            raise ValueError("successful result must not contain an error")
        if not self.success and (not isinstance(self.error, str) or not self.error.strip()):
            raise ValueError("failed result must contain a diagnostic error")
        if not self.success and self.output is not None:
            raise ValueError("failed result must not contain output")
