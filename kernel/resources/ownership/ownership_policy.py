from dataclasses import dataclass


@dataclass(frozen=True)
class OwnershipPolicy:

    allow_transfer: bool
    enforce_exclusive_ownership: bool