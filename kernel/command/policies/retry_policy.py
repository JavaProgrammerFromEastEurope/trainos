from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class RetryPolicy:
    """Retry configuration for a command policy."""

    max_attempts: int
    delay_ticks: int

    def __post_init__(self) -> None:
        if self.max_attempts < 1:
            raise ValueError("max_attempts must be positive")
        if self.delay_ticks < 0:
            raise ValueError("delay_ticks must not be negative")
