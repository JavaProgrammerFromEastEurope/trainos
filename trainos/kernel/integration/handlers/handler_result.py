from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class HandlerResult:

    success: bool
    message: str