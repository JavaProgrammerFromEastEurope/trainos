from dataclasses import dataclass

from kernel.governance.authorities.authority_status import AuthorityStatus


@dataclass(frozen=True, slots=True)
class AuthoritySnapshot:

    authority_id: str
    status: AuthorityStatus
