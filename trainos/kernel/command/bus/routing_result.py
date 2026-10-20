from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class RoutingResult:
    """Outcome of routing a command to a handler.

    Optional fields preserve compatibility with callers that construct the
    original two-field result directly.
    """

    success: bool
    handler_id: str
    command_id: str | None = None
    error: str | None = None

    def __post_init__(self) -> None:
        if not isinstance(self.success, bool):
            raise TypeError("success must be a bool")
        if not isinstance(self.handler_id, str):
            raise TypeError("handler_id must be a string")
        if self.command_id is not None and (not isinstance(self.command_id, str) or not self.command_id.strip()):
            raise ValueError("command_id must be a non-empty string when provided")
        if self.success:
            if not self.handler_id.strip():
                raise ValueError("successful routing requires a handler_id")
            if self.error is not None:
                raise ValueError("successful routing must not contain an error")
        elif not isinstance(self.error, str) or not self.error.strip():
            raise ValueError("failed routing requires a diagnostic error")
