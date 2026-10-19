from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class EventPayload:

    key: 		str
    value: 	str