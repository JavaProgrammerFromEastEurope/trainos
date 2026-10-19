from dataclasses import dataclass

from .diff_result import DiffResult


@dataclass(frozen=True)
class ConstitutionalDiff:

    from_version: str
    to_version: 	str
    result: DiffResult