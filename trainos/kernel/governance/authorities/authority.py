from dataclasses import dataclass

from .authority_status import AuthorityStatus


@dataclass(frozen=True, slots=True)
class Authority:

    authority_id: str
    resident_id: 	str
    status: AuthorityStatus