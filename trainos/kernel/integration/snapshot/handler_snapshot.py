from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class HandlerSnapshot:

    handlers: int