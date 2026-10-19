from dataclasses import dataclass


@dataclass(frozen=True)
class ConstitutionalConflict:

    left_article: str
    right_article: str