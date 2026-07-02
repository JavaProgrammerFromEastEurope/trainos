from dataclasses import dataclass


@dataclass(frozen=True)
class CivilStatus:

    entity_id: str
    status_id: str