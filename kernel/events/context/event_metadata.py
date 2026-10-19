from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class EventMetadata:

    publisher_id: str
    runtime_id: 	str
    tick: 				int
    correlation_id: str
