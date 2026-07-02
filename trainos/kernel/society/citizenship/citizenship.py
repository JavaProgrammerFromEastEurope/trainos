from dataclasses import dataclass

from .citizenship_status import CitizenshipStatus


@dataclass(frozen=True)
class Citizenship:

    entity_id: str
    status: CitizenshipStatus