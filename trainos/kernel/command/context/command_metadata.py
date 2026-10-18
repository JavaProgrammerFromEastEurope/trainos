from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class CommandMetadata:
    """Execution metadata captured when a command enters the system."""

    runtime_id: str
    scheduler_id: str
    tick: int
    correlation_id: str
    source: str

    def __post_init__(self) -> None:
        for field_name in ("runtime_id", "scheduler_id", "correlation_id", "source"):
            if not getattr(self, field_name).strip():
                raise ValueError(f"{field_name} must not be empty")
        if self.tick < 0:
            raise ValueError("tick must not be negative")
