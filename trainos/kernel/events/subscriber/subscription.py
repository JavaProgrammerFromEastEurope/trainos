from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Subscription:

    event_name: str