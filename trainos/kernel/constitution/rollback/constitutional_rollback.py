from dataclasses import dataclass

from .rollback_result import RollbackResult


@dataclass(frozen=True)
class ConstitutionalRollback:

    from_version: 	str
    target_version: str
    result: RollbackResult