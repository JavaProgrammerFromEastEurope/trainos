from .authority import Authority
from .authority_status import AuthorityStatus


class AuthorityEngine:

    def suspend(
        self,
        authority: Authority,
    ) -> Authority:
        return Authority(
            authority_id=authority.authority_id,
            resident_id=authority.resident_id,
            status=AuthorityStatus.SUSPENDED,
        )

    def activate(
        self,
        authority: Authority,
    ) -> Authority:
        return Authority(
            authority_id=authority.authority_id,
            resident_id=authority.resident_id,
            status=AuthorityStatus.ACTIVE,
        )