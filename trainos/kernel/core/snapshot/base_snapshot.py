from dataclasses import dataclass
from typing import Generic, TypeVar

T = TypeVar("T")


@dataclass(frozen=True)
class BaseSnapshot(Generic[T]):

    snapshot_id: str
    timestamp: str
    state: T
