from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class RepositorySnapshot:

    repository_count: int