from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class ExecutionProgress:
    """Progress counters for one command execution."""

    attempts: int
    max_attempts: int
    completed: bool

    def __post_init__(self) -> None:
        if self.attempts < 0:
            raise ValueError("attempts must not be negative")
        if self.max_attempts < 1:
            raise ValueError("max_attempts must be positive")
        if self.attempts > self.max_attempts:
            raise ValueError("attempts cannot exceed max_attempts")
        if not isinstance(self.completed, bool):
            raise TypeError("completed must be a bool")
