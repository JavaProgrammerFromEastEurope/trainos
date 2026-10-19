from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class PersistenceResult:

    success: bool
    data: object | None