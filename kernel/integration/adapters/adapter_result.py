from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class AdapterResult:

    success: bool
    payload: object | None